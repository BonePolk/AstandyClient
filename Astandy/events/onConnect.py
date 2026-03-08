from collections.abc import Callable

from Astandy import listeners

class OnConnect:

    def OnConnect(self) -> Callable:
        """
        **Decorator!** Register callback on connect event
        """
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(listeners.OnConnect(func))

            return func

        return decorator