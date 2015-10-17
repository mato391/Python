__author__ = 'mato3'
import datetime

class Log:

    def __init__(self):
       '''
       Constructor, opening log.txt file. If file is not exists, file will be created.
       :return: None
       '''
       self.hFile = open("log.txt", "w+")

    def __del__(self):
        '''
        Destructor, closing opened files.
        :return: None
        '''
        self.hFile.close()

    def logging(self, info, type):
        '''
        Logging information with date and type of message.
        :return: None
        '''
        message = "[" + type + "] " + str(datetime.datetime.now()) + " " + str(info) + "\t\n"
        self.saveToFile(message)
        print(message)


    def saveToFile(self, log):
        '''
        Writing message to file.
        :return: None
        '''
        self.hFile.write(log)


logger = Log()

