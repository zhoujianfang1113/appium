# coding=utf-8
import yaml
import logging.config
import logging
from time import ctime
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 导入日志配置文件模块配置下面这段代码
CON_LOG = '../config/log.conf'    # log.conf 文件存放的路径
logging.config.fileConfig(CON_LOG)    # 读取日志配置表
logging = logging.getLogger()   # 日志采集器

devices_list = ['7d78b1ff', 'emulator-5554']


# 将启动信息封装成一个方法
def appium_desired(udid,port):
    file = open('../config/desired_caps.yaml', 'r', encoding='UTF-8')  # 导入手机配置文件
    data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['app'] = data['app']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['udid'] = udid
    print('appium port: %s start run %s at %s' %(port,udid,ctime()))
    logging.info('开始启动APP....')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(7)  # 等待 s
    return driver      # 返回设置好的整个driver，及启动APP




# 使用if__name 进行调试 appium_desired 这个方法，别的模块调用这个方法,appium_desired里的内容不会被执行，
# 如果在当前页面执行，会执行appium_desired 里的内容。
if __name__ == '__main__':
    appium_desired(devices_list[0],4723)
    appium_desired(devices_list[1],4726)



