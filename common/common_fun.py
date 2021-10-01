from baseVies.baseView import BaseView    # 导入文件夹下的baseView模块
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
import logging.config
from selenium.webdriver.common.by import By
import time
import os
import random
import csv
from time import sleep


class Common(BaseView):             # Common 自定义
    confirmBtn = (By.ID, 'com.cliff:id/tv_confirm')     # 确定按钮
    libraryBtn = (By.ID, 'com.cliff:id/cl_library')
    mine = (By.ID, 'com.cliff:id/iv_mine')           # [我的]
    settingBtn = (By.ID, 'com.cliff:id/top_setting_iv')  # 设置按钮
    logoutBtn = (By.ID, 'com.cliff:id/tv_logout')  # 退出登录
    text = (By.ID, 'com.cliff:id/edit_text')   # 输入框
    usernameBtn = (By.ID, 'com.cliff:id/et_account')
    passwordBtn = (By.ID, 'com.cliff:id/et_password')
    csgId = (By.ID, 'com.cliff:id/tv_user_csg_id')  # 藏书馆id
    loginBtn = (By.ID, 'com.cliff:id/tv_login')         # 登录
    agreement = (By.ID, 'com.cliff:id/iv_agreement_checkbox')  # 同意协议按钮
    enterBtn = (By.ID, 'com.cliff:id/tv_enter') # 立即体验按钮/立即体验
    headBtn = (By.ID, 'com.cliff:id/user_head_iv')          # 用户头像
    activeBtn = (By.ID, 'com.cliff:id/img_active')  # 活动弹窗
    closeBtn = (By.ID, 'com.cliff:id/img_close')  # 活动弹窗关闭按钮
    coinBtn = (By.ID, 'com.cliff:id/lly_gold_vip')  # 金币按钮
    SeeCoinBtn = (By.ID, 'com.cliff:id/tv_login_see_coin')  # 查看登录
    skipBtn = (By.ID, 'com.cliff:id/tv_skip') # 跳过按钮
    adv_skipBtn = (By.ID, 'com.cliff:id/tt_splash_skip_btn') # 广告跳过按钮
    ad_bar = (By.ID, 'com.cliff:id/tt_splash_bar_text') # 开屏广告
    accountBtn = (By.ID, 'com.cliff:id/et_account') # 账号输入框
    checkboxBtn = (By.ID, 'com.cliff:id/iv_agreement_checkbox') # 阅读并同意用户协议
    homeBtn = (By.ID, 'com.cliff:id/lly_home') # 书馆tab
    textBtn = (By.XPATH, "//*[@text='立即登录']") # “立即登录”字样
    library_head = (By.ID, 'com.cliff:id/iv_library_head')
    vipCardBtn= (By.ID, 'com.cliff:id/mine_card_vip_lay')   # vip 卡片
    backBtn = (By.ID, 'com.cliff:id/iv_back')
    coReadingBtn=(By.XPATH,'//*[@text="共读"and@index="3"]')
    serviceBtn=(By.ID,'com.cliff:id/tv_user_service_agreement_and_privacy_policy') # 阅读并同意服务协议


# 判断是否有开屏广告
    def check_adv(self):
        try:

            self.driver.find_element(*self.adv_skipBtn)
        except NoSuchElementException:
            logging.info('没有广告')

        else:
            self.getScreenShot('开屏广告')
            self.driver.find_element(*self.adv_skipBtn).click()
            logging.info('点击跳过按钮')

# 输入账号与密码并且登陆。
    def Login_action(self,user,password):
        self.driver.find_element(*self.accountBtn).click()
        self.driver.find_element(*self.accountBtn).send_keys(user)
        logging.info('输入账号:%s'%user)
        self.driver.find_element(*self.passwordBtn).send_keys(password)
        logging.info('输入密码:%s'%password)

        self.driver.find_element(*self.checkboxBtn).click()
        self.driver.find_element(*self.loginBtn).click()
        # self.Login_status()
        try:
            self.driver.find_element(*self.vipCardBtn)
        except NoSuchElementException:
            logging.info('不在我的页面')
        else:
            logging.info('点击返回按钮')
            self.driver.find_element(*self.backBtn).click()



# 检测是否有活动弹窗
    def activePop(self):
        try:
            self.driver.find_element(*self.activeBtn)
        except NoSuchElementException:
            logging.info("======没有活动弹窗=====")
        else:
            logging.info("=====关闭活动弹窗=====")
            self.driver.find_element(*self.closeBtn).click()


# 私人图书馆弹窗
#     def check_OpenLibrary(self):
#         try:
#             self.driver.find_element(*self.libraryBtn)
#         except NoSuchElementException:
#             logging.info('用户已经开馆')
#         else:
#             SkipBtn=self.driver.find_element(*self.skipBtn)
#             SkipBtn.click()
#             logging.info('点击跳过按钮')


# 封装获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y
    # 向左滑动
    def swipeleft(self):
        l = self.get_size()
        x1 = int(l[0] * 0.8)  # x起点坐标
        x2 = int(l[0] * 0.05)  # x终点坐标
        y1 = int(l[1] * 0.5)  # 起始y坐标
        y2 = int(l[1] * 0.5)  # 终点y坐标
        self.driver.swipe(x1, y1, x2, y2, 500)   # 此次滑动时间单位毫秒500
        logging.info('向左滑动')

    # 向左滑动
    def swipeUp(self):
        N = self.get_size()
        x1 = int(N[0] * 0.5)  # x起点坐标
        x2 = int(N[0] * 0.5)  # x终点坐标
        y1 = int(N[1] * 0.85)  # 起始y坐标
        y2 = int(N[1] * 0.2)  # 终点y坐标
        self.driver.swipe(x1, y1, x2, y2, 500)  # 此次滑动时间单位毫秒500
        logging.info('向上滑动')

    # 封装，获取当前时间，根据年月日小时分钟秒进行输出。
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

# 封装截图
    # 两个module 自定义，要根据不同模块变化而变化。
    def getScreenShot(self, module):
        time = self.getTime()
        # logging.info('获取当前时间')
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' % (module, time)
        logging.info('start getScreenshot %s' %module)
        # 保存到指定的文件路径
        self.driver.get_screenshot_as_file(image_file)

# 封装一个数据读取方法封装
    # import csv
    def get_csv_data(self, csv_file, line):
        logging.info('=====获取csv文件数据=====')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):      # 1默认读取数据从第一行开始
                if index == line:
                    return row
# 调用：
#     csv_file='../data/account.csv'
#     data=get_csv_data((csv_file,3))    # 3代表读取列表中的第三行数据
#     print(data[0],data[1])    # data[0]，data[1],代表上面第三行的第一组数据和第二组数据。




# 封装一个退出登录步骤
    def logout_action(self):
        self.driver.find_element(*self.mine).click()
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.confirmBtn).click()
# 输入随机昵称
    def random_text(self):
        self.driver.find_element(*self.text).clear()
        nick = '凉风有信秋月无边' + str(random.randint(1, 100))
        self.driver.find_element(*self.text).send_keys(nick)
        self.driver.find_element(*self.confirmBtn).click()

    # 在登录页面判断是否已登录。
    def check_login1(self):
        try:
            self.driver.find_element(*self.serviceBtn)
        except NoSuchElementException:
            logging.info('已登录')
        else:
            self.Login_action('13850338329','123456')



# 判断是否已登录，其他不做操作。
    def Login_status(self):
        try:
            self.driver.find_element(*self.loginBtn)
        except NoSuchElementException:
            logging.info('======已登录=====')
            self.getScreenShot('已登录')
            return True
        else:
            logging.info('======登录失败=======')
            self.getScreenShot('登录失败')
            return False




if __name__== '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_adv()
    com.getScreenShot('zjf')  # 括号内要写上所要截图的模块,记住引号。
    # com.check_OpenLibrary()
    com.swipeleft()
    com.Login_action('19524239612','123456')
    com.activePop()
    com.logout_action()
    com.random_text()
    com.get_csv_data()
    com.Login_status()

    com.swipeUp()








