from selenium import webdriver
from AL.page.al_page import al_pages
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest,logging,ddt
from AL.text.rizhi import rizhi
a=rizhi('1.txt')
a.get_log()
from ddt import ddt,data,unpack
from AL.text.ddts import lei
a=lei()


from time import sleep

class al_texts(unittest.TestCase):
    def setUp(self) -> None:
        pass
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome(r'C:\Users\86176\Desktop\chromedriver.exe')
        cls.driver.get('https://www.1688.com/')

    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test01(self):#登录测试用例1
        'dd'
    # al_pages(self.driver).al_cz()
        self.assertNotIn('152','1')#一种断言
    @data(*unpack(*data()))
    def test02(self):#找货源用例2
        logging.info('开始')
        al_pages(self.driver).al_cz2()
        # self.driver.switch_to.frame('login_iframe')#ifname框架
        self.assertIsNotNone('ss')#二种断言
        logging.info('结束')
    def test03(self):#找工厂用例3
        '12'
        # al_pages(self.driver).gyp_cz()
        self.assertIsNot('15','dd')#三种断言
    def test04(self):#收藏
        '36'
        # al_pages(self.driver).ghs_cz()
    def test05(self):#供货商
        '12'
        # al_pages(self.driver).ghs_cz()
if __name__ == '__main__':
    unittest.TestCase()