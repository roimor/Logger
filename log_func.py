import logging
import time
import datetime

print ('pizza')
class Logger:
    def __init__(self):
        self.ts = time.time()
        self.st = datetime.datetime.fromtimestamp(self.ts).strftime('%Y-%m-%d %H:%M:%S')
        logging.basicConfig(filename='log_file.log', level=logging.INFO)

    def start(self, text, st):
        logging.info(st + "==>" + text)

    def success(self, text, st):
        logging.info(st + "==>" + text)

    def run(self,text):
        self.start(text,self.st)
