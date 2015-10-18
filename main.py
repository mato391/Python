__author__ = 'mato3'

from Log import *
from strings import *
from Constance import *
from Config import *
from GUI import *

def main():
    LOGGER.logging(welcome["StartProgram"])
    configure()
    createWindow()

def configure():
    c = Config()
    LOGGER.logging("Set flags: " + str(c.flags), "DEBUG")

def createWindow():
    app = wx.App()
    Window(None, title=windowTitle["main"], size=windowSize)
    app.MainLoop()

if __name__ == '__main__':
    main()
