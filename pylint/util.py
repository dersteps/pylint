import os
from os.path import expanduser
from os import path, makedirs
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_user_home():
    return expanduser('~')

def get_pylint_home():
    return path.join(get_user_home(), ".pylint")

def get_plugins_directory():
    return path.join(get_pylint_home(), "plugins")

def ensure_pylint_home():
    directory = get_pylint_home()
    if not path.exists(directory):
        logger.debug("PyLint home does not exist, creating it")
        makedirs(directory)
    else:
        logger.debug("PyLint home exists")

def ensure_pylint_plugins_dir():
    directory = get_plugins_directory()
    if not path.exists(directory):
        logger.debug("PyLint plugin directory does not exist, creating it")
        makedirs(directory)
    else:
        logger.debug("PyLint plugin directory exists")

def check_os():
    '''
    Determines the underlying operating system, which comes in handy when using
    colors. On Windows systems, no color codes are used. Posix systems use ANSI
    color codes.
    '''
    if os.name == "nt": return "windows"
    if os.name == "posix": return "posix"

if check_os() == "posix":
    class bcolors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'
        backBlack = '\033[40m'
        backRed = '\033[41m'
        backGreen = '\033[42m'
        backYellow = '\033[43m'
        backBlue = '\033[44m'
        backMagenta = '\033[45m'
        backCyan = '\033[46m'
        backWhite = '\033[47m'

# if we are windows or something like that then define colors as nothing
else:
    class bcolors:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERL = ''
        ENDC = ''
        backBlack = ''
        backRed = ''
        backGreen = ''
        backYellow = ''
        backBlue = ''
        backMagenta = ''
        backCyan = ''
        backWhite = ''

def s(text):
    print "[%s+%s] %s" % (bcolors.GREEN, bcolors.ENDC, text)

def i(text):
    print "[%s*%s] %s" % (bcolors.CYAN, bcolors.ENDC, text)

def w(text):
    print "[%s!%s] %s" % (bcolors.YELLOW, bcolors.ENDC, text)

def e(text):
    sys.stderr.write("[%s!%s] %s\n" % (bcolors.RED, bcolors.ENDC, text))
