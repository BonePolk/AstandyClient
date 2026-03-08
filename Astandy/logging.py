import logging

from .types.extras import Extra, ConnectionInfo

class AstandyLoggers:
    class Adapter(logging.LoggerAdapter):
        def __init__(self, logger):
            super(AstandyLoggers.Adapter, self).__init__(logger, {})
            self.extra: Extra = Extra()

        def process(self, msg, kwargs):
            if issubclass(self.extra.__class__, Extra) and Extra != self.extra.__class__:
                return '[%s] - %s' % (self.extra, msg), kwargs
            else:
                return msg, kwargs
        
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        return AstandyLoggers.Adapter(logger)