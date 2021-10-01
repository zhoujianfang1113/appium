from appium import webdriver
import yaml
# coding=utf-8
file = open('desired_caps.yaml', 'r', encoding='UTF-8')
data = yaml.load(file, Loader=yaml.FullLoader)

desired_caps={}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']
desired_caps['app'] = data['app']
desired_caps['appActivity'] = data['appActivity']
desired_caps['noReset'] = data['noReset']
desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
desired_caps['resetKeyboard'] = data['resetKeyboard']
desired_caps['resetKeyboard'] = data['resetKeyboard']
# desired_caps['udid'] = data['udid']
driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
