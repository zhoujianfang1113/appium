from common.common_fun import Common
import logging
from common.desired_caps import appium_desired
from time import sleep

class uni_test(Common):

    def login_uni(self,user,password):
        self.check_adv()
        self.check_confirm()
        self.driver.find_element(*self.accountBtn).click()
        self.driver.find_element(*self.accountBtn).send_keys(user)
        logging.info('输入账号:%s' % user)
        self.driver.find_element(*self.passwordBtn).send_keys(password)
        logging.info('输入密码:%s' % password)

        self.driver.find_element(*self.checkboxBtn).click()
        self.driver.find_element(*self.loginBtn).click()
        sleep(1)
        self.getScreenShot('登录')

if __name__ == '__main__':
    driver=appium_desired()
    l=uni_test(driver)
    l.login_uni('15627558990','123456')
