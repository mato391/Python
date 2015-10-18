__author__ = 'Mato3'
import sys
import os
from strings import *
from Log import *

class Config:

    text = ""
    def __init__(self):
        '''
        Loading swconfig file with flags
        :return: None
        '''
        self.hFile = open("swconfig.txt", "r+")
        self.content = self.hFile.readlines()
        self.parseForFlags()


    def __del__(self):
        '''
        Destructor
        :return: None
        '''
        self.hFile.close()

    def parseForFlags(self):
        '''
        Parsing swconfig file
        :return: None
        '''
        flags=[]
        values=[]
        for element in self.content:
            hashIndex = element.find("#", 0, len(element))
            if hashIndex != 0 and hashIndex != -1:
                element = element[:hashIndex]
                flags.append(element.split("=")[0])
                values.append(element.split("=")[1].replace("\n", ""))
            elif hashIndex != 0:
                flags.append(element.split("=")[0])
                values.append(element.split("=")[1].replace("\n", ""))
        self.flags = dict(zip(flags, values))
        LOGGER.logging("swconfig file loaded", "INFO")

    def isFlagSet(self, name, value="1"):
        '''
        This function checks flag by name and value.
        :return: Boolean
        '''
        for flag in self.flags:
            if name == flag:
                if value == self.flags[flag]:
                    return True
        return False
    '''
    def setFlag(self, name, value="1"):
        self.flags[name] = value
        self.save()
    '''

    def deleteFlag(self, name):
        '''
        This function deletes given flags from file.
        :return: None
        '''
        if name in self.flags:
            del self.flags[name]
        self.save()

    def save(self):
        '''
        This function swrites to file changes.
        :return: None
        '''
        for flag in self.flags:
            self.text += flag + "=" + self.flags[flag] + "\n"
        self.hFile.write(self.text)
        self.askForReset()

    def restartProgram(self):
        '''
        This function resets program
        :return: None
        '''
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def askForReset(self):
        '''
        This function asks user about required reset program. If User answer "yes" program will be restart. Other way
        program will be contious work.
        :return: None
        '''
        answer = raw_input(askForReset["askForReset"])
        if answer.lower().strip() in "y yes".split():
            self.restartProgram()
        elif answer.lower().strip() in "n no".split():
            print(askForReset["noReset"])
        else:
            print(askForReset["invalidAnswer"])


def main():
    LOGGER.logging(welcome["StartProgram"], "INFO")
    c = Config()
    LOGGER.logging("Set flags: " + str(c.flags), "DEBUG")
    LOGGER.logging(c.isFlagSet("0x01", "0"), "DEBUG")
    if c.isFlagSet("0x01"):
        LOGGER.logging("Debuging message", "DEBUG")



if __name__ == '__main__':
    main()