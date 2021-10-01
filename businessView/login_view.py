from common.desired_caps import appium_desired    # 导入启动APP模块
from common.common_fun import Common   # 导入封装方法
from selenium.webdriver.common.by import By
import logging
from selenium.common.exceptions import NoSuchElementException
from businessView import Check_Confirm

class Prod_login(Common,Check_Confirm):
    enterBtn = (By.ID, 'com.cliff:id/tv_enter')   # 立即体验按钮

    def LoginAction(self,user,password):

        self.driver.find_element(*self.accountBtn).click()
        self.driver.find_element(*self.accountBtn).send_keys(user)
        logging.info('输入账号:%s' % user)
        self.driver.find_element(*self.passwordBtn).send_keys(password)
        logging.info('输入密码:%s' % password)
        self.driver.find_element(*self.checkboxBtn).click()
        self.driver.find_element(*self.loginBtn).click()
        self.Login_status()
    def LOGIN(self):
        self.check_adv()
        self.check_confirm()



    def check_OpenLibrary(self):
        try:
            self.driver.find_element(*self.libraryBtn)
        except NoSuchElementException:
            logging.info('没有进入开馆页面')
        else:
            SkipBtn = self.driver.find_element(*self.skipBtn)
            SkipBtn.click()
            logging.info('点击跳过按钮')





if __name__ == '__main__':
    driver = appium_desired()
    l= Prod_login(driver)
    l.LOGIN()
    # l.check_OpenLibrary()
