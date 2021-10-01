from businessView.Check_Confirm import Confirm
from selenium.common.exceptions import NoSuchElementException
import logging
from common.desired_caps import appium_desired

class Sim_Login(Confirm):

    def sim_login(self):
        self.check_adv()
        self.check_confirm()
        # 判断是否登录
    def check_login(self):
        self.driver.find_element(*self.homeBtn).click()
        logging.info('点击[书馆]页面')
        try:
            self.driver.find_element(*self.textBtn)
        except NoSuchElementException:
            logging.info('已经登录')
        else:
            self.driver.find_element(*self.library_head).click()
            self.driver.find_element(*self.headBtn).click()
            self.Login_action('13850338329','123456')


if __name__ == '__main__':
    driver=appium_desired()
    i=Sim_Login(driver)
    i.sim_login()
    i.check_login()

