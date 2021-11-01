from selenium.webdriver.common.by import By
from time import sleep
from AL.base.base_page import Base_pages
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class al_pages(Base_pages):
    url='https://www.1688.com/'
    #登录定位元素
    al_dj=(By.XPATH,'//*[@id="alibar"]/div[1]/div[2]/ul/li[3]/a')#一种定位
    al_sr=(By.CLASS_NAME,'fm-text')#二种定位
    al_sr2=(By.ID,'fm-login-password')#三种定位
    al_dj2=(By.XPATH,'//*[@id="login-form"]/div[4]/button')
    #找货源元素定位
    al_ss=(By.XPATH,'//*[@id="pc-new-main-box"]/div[1]/div[2]/ul/li[1]/div/span/div/div/a[1]')
    al_ddj=(By.CLASS_NAME,'desc-text')
    al_ddj2=(By.XPATH,'//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/div/div[2]/div[2]/table/tbody/tr[2]/'
                      'td[4]/div/div/input')
    al_ssr=(By.XPATH,'//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/d'
                      'iv/div[2]/div[2]/table/tbody/tr[2]/td[4]/div/div/input')
    # al_ddj3=(By.XPATH,'//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/div/div[5]/div[1]/a[2]/span')
    #找工厂业品元素
    # gyp_dj=(By.XPATH,'//*[@id="search-tab-wrap"]/div/section/div[1]/div[3]/p')
    # gyp_dj2=(By.CLASS_NAME,'f-14 c-name')
    # gyp_dj3=(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div[9]/div/div/div[2]/div[1]/div/a[1]/div/div[1]/img')
    # gyp_dj4=(By.ID,'a260j.12536222.k8ii902p.i0.12b678c5IEovHo')
    # gyp_dj5=(By.XPATH,'//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/div/div[1]/div[2]/table/tbody/tr/td[4]/div/div/a[2]')
    # gyp_dj6=(By.XPATH,'//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/div/div[4]/div[1]/a[2]/span')
    #收藏定位元素
    # sc_dj=(By.XPATH,'//*[@id="search-tab-wrap"]/div/section/div[1]/div[3]/p')
    # sc_dj2=(By.CLASS_NAME,'f-14 c-name')
    # sc_dj3=(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div[9]/div/div/div[2]/div[1]/div/a[1]/div/div[1]/img')
    # sc_dj4=(By.ID,'a260j.12536222.k8ii902p.i0.12b678c5IEovHo')
    # sc_dj5=(By.PARTIAL_LINK_TEXT,'收藏')#五种定位
    # sc_dj6=(By.XPATH,'//*[@id="mod-detail-bd"]/div[1]/div/div/div/div/div[3]/div/a')#查看是否有收藏




    #供货商元素定位
    ghs_dj=(By.XPATH,'//*[@id="search-tab-wrap"]/div/section/div[1]/div[3]/p')
    ghs_dj2=(By.CLASS_NAME,'f-14 c-name')
    ghs_dj3=(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div[9]/div/div/div[2]/div[1]/div/a[1]/div/div[1]/img')
    ghs_dj4=(By.ID,'a260j.12536222.k8ii902p.i0.12b678c5IEovHo')
    ghs_dj5=(By.PARTIAL_LINK_TEXT,'收藏')
    _dghsj6=(By.NAME,'//*[@id="mod-detail-bd')#四种定位














    # def al_cz(self):
    #     self.get_url(self.url)
    #     self.click_ele(self.al_dj)
    #     self.driver.maximize_window()#最大化窗口
    #
    #     self.send_keys_ele(self.al_sr,'zgh17851815396')
    #     self.send_keys_ele(self.al_sr2,'zgh.123456')
    #     self.click_ele(self.al_dj2)
    def al_cz2(self):
        self.click_ele(self.al_ss)
        self.driver.maximize_window()
        self.driver.switch_to.window(self.driver.window_handles[-1])#多窗口切换
        sleep(2)#一种等待
        self.click_ele(self.al_ddj)
        # self.click_ele(self.al_ddj2)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        self.driver.find_element_by_xpath('//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/div/div[2]/div[2]/table/'
                                          'tbody/tr[2]/td[4]/div/div/input').send_keys(Keys.CONTROL,'a')#键盘操作
        self.driver.find_element_by_xpath('//*[@id="mod-detail-bd"]/div[2]/div[13]/div/div/div/div[2]/div[2]/table/'
                                          'tbody/tr[2]/td[4]/div/div/input').send_keys(Keys.DELETE)  # 键盘操作
        self.send_keys_ele(self.al_ssr,'2')
    #     self.driver.implicitly_wait(6)#二种等待
    #     self.click_ele(self.al_ddj3)#查看购物车
    # def gyp_cz(self):
    #     self.click_ele(self.gyp_dj)
    #     self.click_ele(self.gyp_dj2)
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     self.click_ele(self.gyp_dj3)
    #     self.click_ele(self.gyp_dj4)
    #     self.click_ele(self.gyp_dj5)
    #     self.click_ele(self.gyp_dj6)#查看购物车
    # def sc_cz(self):
    #             self.click_ele(self.sc_dj)
    #             self.click_ele(self.sc_dj2)
    #             self.driver.switch_to.window(self.driver.window_handles[-1])
    #             self.click_ele(self.sc_dj3)
    #             self.click_ele(self.sc_dj4)
    #             self.send_keys_ele(self.sc_dj5,'收藏')
    # def ghs_cz(self):
    #     self.click_ele(self.ghs_dj)
    #     self.click_ele(self.ghs_dj2)
    #     a = WebDriverWait(self.driver, 10, 0.5).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="alibar"]/div[1]/div[2]/ul/li[3]/a')))
    #     a.click()#三种等待
    #
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     self.click_ele(self.ghs_dj3)
    #     self.click_ele(self.ghs_dj4)
    #     self.send_keys_ele(self.ghs_dj5,'')













