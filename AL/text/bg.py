import unittest
from BeautifulReport import BeautifulReport




if __name__ == '__main__':
    a=unittest.defaultTestLoader.discover('./',pattern='al_text.py')
    b=BeautifulReport(a)
    b.report(filename='阿里测试报告',description='这是一个阿里测试报告')


