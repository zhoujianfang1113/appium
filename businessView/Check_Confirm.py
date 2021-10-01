from selenium.common.exceptions import NoSuchElementException
import logging
from time import sleep
from common.desired_caps import appium_desired
from common.common_fun import Common

# 判断是否有同意协议弹窗

class Confirm(Common):

    def check_confirm(self):

        try:
            confirmBtn = self.driver.find_element(*self.confirmBtn)
        except NoSuchElementException:
            logging.info('非首次打开APP')
        else:
            self.getScreenShot('同意按钮')
            confirmBtn.click()
            logging.info('点击同意按钮')
            sleep(2)
            for i in range(4):
                self.swipeleft()
                sleep(0.5)
            self.getScreenShot('立即体验')
            self.find_element(*self.enterBtn).click()  # 点击[立即体验]按钮
            self.Login_action('15627558993','123456')

if __name__ == '__main__':
    driver=appium_desired()
    l=Confirm(driver)
    l.check_confirm()
