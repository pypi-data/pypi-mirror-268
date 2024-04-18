import logging

class HuemulLogging:
    def __init__(self):
        FORMAT = '%(asctime)s %(message)s'
        logging.basicConfig(format=FORMAT, level=logging.INFO)
        self.logger = logging.getLogger('Enola')

    #
    # logMessageDebug: Send {message} to log4j - Debug
    #
    def logMessageDebug(self, message):
        self.logger.debug(message)

    #
    # logMessageInfo: Send {message} to log4j - Info
    #
    def logMessageInfo(self, message):
        self.logger.info(message)

    #
    # logMessageWarn: Send {message} to log4j - Warning
    #
    def logMessageWarn(self, message):
        self.logger.warn(message)

    #
    # logMessageError: Send {message} to log4j - Error
    #
    def logMessageError(self, message):
        self.logger.error(msg = str(message), extra={"error": message})