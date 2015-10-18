__author__ = 'mato3'
'''
Main file to run program.
'''
from Log import *
from strings import *
from Constance import *
from Config import *
from GUI import *

def main():
    LOGGER.logging(welcome["StartProgram"])
    c = Config()
    LOGGER.logging("Set flags: " + str(c.flags), "DEBUG")
    createWindow()


def createWindow():
    app = wx.App()
    Window(None, title=windowTitle["main"], size=windowSize)
    app.MainLoop()

if __name__ == '__main__':
    main()
