# -*- coding: utf-8 -*-
# @Time    : 2020-10-21 10:37
# @Author  : baiping


from selenium import webdriver

class Login():
    driver = None
    # def __init__(self):
    #打开浏览
    def open_browser(self,name='chrome'):
        if name == 'chrome':
            self.driver = webdriver.Chrome("C:\\Users\\60558\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
        elif name =='firefox':
            self.driver = webdriver.Firefox()
        else:
            pass
        Login.driver=self.driver

        self.driver.get('http://www.summermori.icu:8080/JavaPrj_6/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    #关闭浏览器
    def close_browser(self):
        self.driver.quit()

    def login(self,username,password):
        self.driver.find_element_by_id('UserName').send_keys(username)
        self.driver.find_element_by_id('Password').send_keys(password)
        self.driver.find_element_by_name('submit').click()

    def test_login_null(self):
        self.login('','')
        error_text = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td').text
        if error_text=='请勿非法登录！':
            print('pass')
        else:
            print('failed')


    def test_login_error(self):
        pass

    def test_succes(self):
        self.login('admin','4444')
        self.driver.switch_to.frame('main')
        text=self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/span').text
        if text =='欢迎使用报价管理系统':
            print('pass')
        else:
            print('failed')

if __name__=='__main__':
    login = Login()
    login.open_browser()
    login.login('admin','4444')

    login.close_browser()




