from selenium import webdriver


class Base_pages():
    def __init__(self,driver):
        self.driver=driver

    def get_url(self,base_url):
        self.driver.get(base_url)




    def find_ele(self,str):
        self.driver.find_element(*str)

    def click_ele(self,str):
        self.driver.find_element(*str).click()

    def send_keys_ele(self,str,text):
        self.driver.find_element(*str).send_keys(text)
