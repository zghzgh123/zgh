import logging

class rizhi():
    def __init__(self,name):
        self.name=name
    def get_log(self):
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)

        fh=logging.FileHandler(self.name,mode='w',encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        ft=logging.Formatter('%(asctime)s -- %(funcName)s -- %(levelname)s -- %(message)s')
        fh.setFormatter(ft)

        logger.addHandler(fh)



