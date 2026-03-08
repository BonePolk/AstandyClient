import asyncio
import sys
import platform
import importlib
from collections.abc import Coroutine

def run_on_uvloop(func: Coroutine, *args, **kwargs):
    if platform.system() == 'Windows':
        print("It is recommended to use Linux with uvloop for better performance.")
        asyncio.run(func)
        return 

    try:
        import uvloop
        
        if sys.version_info >= (3, 11):
            with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
                runner.run(func)
        else:
            uvloop.install()
            asyncio.run(func)
    except ImportError:
        if platform.system() == 'Linux':
            print("It is recommended to install uvloop for better performance on Linux.")
        asyncio.run(func)
        
