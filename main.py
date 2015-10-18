__author__ = 'mato3'

from Log import *
from strings import *
from Config import *

def main():
    LOGGER.logging(welcome["StartProgram"], "INFO")
    c = Config()
    LOGGER.logging("Set flags: " + str(c.flags), "DEBUG")
    if c.isFlagSet("0x01"):
        LOGGER.logging("Debuging message", "DEBUG")



if __name__ == '__main__':
    main()
