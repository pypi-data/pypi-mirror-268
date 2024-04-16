import asyncio
import logging
import time
import inspect

from pydantic import BaseModel

from komoutils.core.base.komo_base import KomoBase
from komoutils.core.base.publish_queue import PublishQueue


class SubscribeRequest(BaseModel):
    type: str = ""
    topics: list = []
    heartbeat: bool = True


class TradeRecord(BaseModel):
    data: tuple = [float, float, float, float, str, int]  # price, amount, trade_ts, age, symbol, identifier
    topic: str = ""
    timestamp: str = ""


async def safe_wrapper(c):
    try:
        return await c
    except asyncio.CancelledError:
        raise
    except Exception as e:
        logging.getLogger(__name__).error(f"Unhandled error in background task: {str(e)}", exc_info=True)
        raise e


def safe_ensure_future(coro, *args, **kwargs):
    return asyncio.ensure_future(safe_wrapper(coro), *args, **kwargs)


async def safe_gather(*args, **kwargs):
    try:
        return await asyncio.gather(*args, **kwargs)
    except Exception as e:
        logging.getLogger(__name__).debug(f"Unhandled error in background task: {str(e)}", exc_info=True)
        raise e


async def wait_til(condition_func, timeout=10):
    start_time = time.perf_counter()
    while True:
        if condition_func():
            return
        elif time.perf_counter() - start_time > timeout:
            raise Exception(f"{inspect.getsource(condition_func).strip()} condition is never met. Time out reached.")
        else:
            await asyncio.sleep(0.1)


async def run_command(*args):
    process = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout.decode().strip()


__all__ = [
    "safe_ensure_future",
    "SubscribeRequest",
    "KomoBase",
    "PublishQueue"
]
