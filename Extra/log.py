import logging
import inspect

class Logger_():

    #def __init__(self, in_file=True):
    def __init__(self, in_file=True):

        self.logger = logging.getLogger("config-debug.log")
        (frame, filename, lineno,
        function_name, msg, index) = inspect.getouterframes(inspect.currentframe())[2]

        #print(func)
        self.logger.setLevel(logging.DEBUG)

        if in_file:

            self.stream_handler = logging.FileHandler(self.logger.name, mode='w')

        else:

            self.stream_handler = logging.StreamHandler()

        log_format = "[%(levelname)s][{0}:{1} - {2}() ] %(message)s".format(filename, lineno, function_name)

        formatter = logging.Formatter(log_format)
        self.stream_handler.setFormatter(formatter)

        self.logger.addHandler(self.stream_handler)
        self.stream_handler.emit = self.decorate_emit(self.stream_handler.emit)

    def decorate_emit(self, fn):

    # add methods we need to the class
        def new(*args):

            levelname = args[0].levelname

            if(levelname == "CRITICAL"):

                color = '\033[31;1m'

            elif(levelname == "ERROR"):

                color = '\033[31;1m'

            elif(levelname == "WARNING"):

                color = '\033[33;1m'

            elif(levelname == "INFO"):

                color = '\033[32;1m'

            elif(levelname == "DEBUG"):

                color = '\033[35;1m'

            else:

                color = '\033[0m'
            # add colored *** in the beginning of the message
            color_levelname = "{0}{1}\033[0m".format(color, levelname)
            args[0].levelname = color_levelname
            # new feature i like: bolder each args of message
            return fn(*args)
        return new


a = Logger_()

def DEBUG(*args):

    a.logger.debug(*args)

def INFO(*args):

    a.logger.info(*args)

def WARNING(*args):

    a.logger.warning(*args)

def ERROR(*args):

    a.logger.error(*args)

def CRITICAL(*args):

    a.logger.critical(*args)

#class DEBUG(Logger_):
#
#    def __init__(self, *args):
#
#        Logger_.__init__(self)
#        self.logger.debug(*args)
#
#    def __call__(self, *args):
#
#        Logger_.__init__(self)
#        self.logger.debug(*args)
#
#class INFO(Logger_):
#
#    def __init__(self, *args):
#
#        Logger_.__init__(self)
#        self.logger.info(*args)
#
#class WARNING(Logger_):
#
#    def __init__(self, *args):
#
#        Logger_.__init__(self)
#        self.logger.warning(*args)
#
#class ERROR(Logger_):
#
#    def __init__(self, *args):
#
#        Logger_.__init__(self)
#        self.logger.error(*args)
#
#class CRITICAL(Logger_):
#
#    def __init__(self, *args):
#
#        Logger_.__init__(self)
#        self.logger.critical(*args)
#
#
################################################################################
#def setup_logger(logger, in_file=True):
#    func = inspect.currentframe().f_back.f_code
#    logger.setLevel(logging.DEBUG)
#    if in_file:
#        sh = logging.FileHandler(logger.name, mode='w')
#    else:
#        sh = logging.StreamHandler()
#    log_format = "[%(levelname)-19s][%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"
#    formatter = logging.Formatter(log_format)
#    sh.setFormatter(formatter)
#    ############################################################################
#    #
#    # TODO: color levelname
#    #
#    ############################################################################
#    def decorate_emit(fn):
#    # add methods we need to the class
#        def new(*args):
#            levelname = args[0].levelname
#            #print(levelname)
#            if(levelname == "CRITICAL"):
#                color = '\x1b[31;1m'
#            elif(levelname == "ERROR"):
#                color = '\x1b[31;1m'
#            elif(levelname == "WARNING"):
#                color = '\x1b[33;1m'
#            elif(levelname == "INFO"):
#                color = '\x1b[32;1m'
#            elif(levelname == "DEBUG"):
#                color = '\x1b[35;1m'
#            else:
#                color = '\x1b[0m'
#            # add colored *** in the beginning of the message
#            color_levelname = "{0}{1}\x1b[0m".format(color,levelname)
#            args[0].levelname = color_levelname
#            # new feature i like: bolder each args of message
#            args[0].args = tuple('\x1b[1m' + arg + '\x1b[0m' for arg in args[0].args)
#            return fn(*args)
#        return new
#
#    sh.emit = decorate_emit(sh.emit)
#    logger.addHandler(sh)
### file name = __name__
##logger = logging.getLogger(__name__)
#logger = logging.getLogger("config-debug.log")
#setup_logger(logger)
#global DEBUG
#global INFO
#global WARNING
#global ERROR
#global CRITICAL
#
#DEBUG    = logger.debug
#INFO     = logger.info
#WARNING  = logger.warning
#ERROR    = logger.error
#CRITICAL = logger.critical
