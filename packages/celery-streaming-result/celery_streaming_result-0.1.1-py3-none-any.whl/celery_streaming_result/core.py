import time
import asyncio
from asgiref.sync import sync_to_async
import msgpack

__all__ = [
    "DEFAULT_ENDED_CHUNK",
    "ReadCeleryStreamingResultTimeout",
    "CeleryStreamingResultManager",
    "start_celery_task_async",
    "get_celery_task_result_async",
]

DEFAULT_ENDED_CHUNK = "this:is:the:celery:streaming:result:ended:chunk:b53127b4-ba43-4ff4-aba4-2134b17b9006"


class ReadCeleryStreamingResultTimeout(RuntimeError):
    args = (124, "读取分片结果超时")


class CeleryStreamingResultManager(object):
    """Celery任务结果分片管理类。

    ## 使用方法

    ```
    csrm = CeleryStreamingResultManager(redis_instance)

    # in task main
    csrm.append_result_chunk(celery_task_instance, result_chunk1)
    csrm.append_result_chunk(celery_task_instance, result_chunk2)
    csrm.append_ended_chunk(celery_task_instance)

    # in task creator process
    async_result = celery_task.delay(*args, **kwargs)
    for chunk in csrm.get_result_chunks(async_result):
        yield chunk
    ```

    ## 支持async_xxx方法

    支持async_xxx方法的前提是store支持async方法。
    要求store实例是由aioredis创建而来。

    aioredis引用方法：
    from redis import asyncio as aioredis

    """

    def __init__(
        self,
        store,
        result_key_template=None,
        ended_chunk=None,
        encode=None,
        decode=None,
        expires=60 * 60 * 24,
    ):
        """基于Redis的Celery任务结果分片管理器。

        @parameter: store Redis实例。
        @parameter: result_key_template 结果缓存键模板。
            默认为：celery-streaming-results:{task_id}。
        @parameter: ended_chunk 分片结束标识。
        @parameter: encode 结果编码。
            默认为：msgpack.dumps
        @parameter: decode 结果解码。
            默认为：msgpack.loads
        @parameter: expires 异常结果保存时间。
            结果被正常取走后，数据也将从redis中删除。
            只有异常没有被正确取走的结果，才会保留在redis中。
            设置一个超时时间，避免有效数据在redis积累造成内存泄漏。
        """
        self.store = store
        self.result_key_template = (
            result_key_template or "celery-streaming-results:{task_id}"
        )
        self.ended_chunk = ended_chunk or DEFAULT_ENDED_CHUNK
        if encode is None:
            self.encode = msgpack.dumps
        else:
            self.encode = encode
        if decode is None:
            self.decode = msgpack.loads
        else:
            self.decode = decode
        self.expires = expires

    def append_result_chunk(self, task, chunk):
        """输出分片结果。"""
        result_key = self.result_key_template.format(task_id=task.request.id)
        self.store.lpush(result_key, self.encode(chunk))
        self.store.expire(result_key, self.expires)

    async def async_append_result_chunk(self, task, chunk):
        """输出分片结果。"""
        result_key = self.result_key_template.format(task_id=task.request.id)
        await self.store.lpush(result_key, self.encode(chunk))
        await self.store.expire(result_key, self.expires)

    def append_ended_chunk(self, task):
        """输出分片结果结束标识。"""
        result_key = self.result_key_template.format(task_id=task.request.id)
        self.store.lpush(result_key, self.encode(self.ended_chunk))
        self.store.expire(result_key, self.expires)

    async def async_append_ended_chunk(self, task):
        """输出分片结果结束标识。"""
        result_key = self.result_key_template.format(task_id=task.request.id)
        await self.store.lpush(result_key, self.encode(self.ended_chunk))
        await self.store.expire(result_key, self.expires)

    def get_result_chunks(
        self,
        celery_async_task,
        total_timeout=0,
        read_timeout=0,
        interval=1,
        on_finished=None,
    ):
        """读取分片结果。

        @parameter: celery_async_task Celery task delay后返回的AsyncTask实例。
        @parameter: total_timeout 总超时时长。超过后，强制结束。
        @parameter: read_timeout 连续没有响应导致的超时时长。超过后，强制结束。
        @parameter: interval 单次读取超时时间。
        @parameter: on_finished 读取结束时的回调。
        """
        stime = time.time()
        rtime = None
        result_key = self.result_key_template.format(task_id=celery_async_task.task_id)
        while True:
            result = self.store.brpop(result_key, timeout=interval)
            if (total_timeout != 0) and (time.time() - stime > total_timeout):
                raise ReadCeleryStreamingResultTimeout()
            if result is None:
                if rtime is None:
                    rtime = time.time()
                else:
                    if (read_timeout != 0) and (time.time() - rtime > read_timeout):
                        raise ReadCeleryStreamingResultTimeout()
            else:
                rtime = None
            if result is None:
                continue
            result = self.decode(result[1])
            if result != self.ended_chunk:
                yield result
            else:
                if on_finished:
                    on_finished(celery_async_task)
                return

    async def async_get_result_chunks(
        self,
        celery_async_task,
        total_timeout=0,
        read_timeout=0,
        interval=1,
        on_finished=None,
    ):
        stime = time.time()
        rtime = None
        result_key = self.result_key_template.format(task_id=celery_async_task.task_id)
        while True:
            result = await self.store.brpop(result_key, timeout=interval)
            if (total_timeout != 0) and (time.time() - stime > total_timeout):
                raise ReadCeleryStreamingResultTimeout()
            if result is None:
                if rtime is None:
                    rtime = time.time()
                else:
                    if (read_timeout != 0) and (time.time() - rtime > read_timeout):
                        raise ReadCeleryStreamingResultTimeout()
            else:
                rtime = None
            if result is None:
                continue
            result = self.decode(result[1])
            if result != self.ended_chunk:
                yield result
            else:
                if on_finished:
                    await on_finished(celery_async_task)
                return


async def start_celery_task_async(celery_task, *args, **kwargs):
    """使用异步方法启动一个Celery任务。"""
    result = await sync_to_async(celery_task.delay)(*args, **kwargs)
    return result


async def get_celery_task_result_async(celery_task_async, *args, **kwargs):
    """获取celery TaskAsync的执行结果。"""
    result = await sync_to_async(celery_task_async.get)(*args, **kwargs)
    return result
