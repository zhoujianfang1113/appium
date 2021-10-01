import unittest
import logging
from common.desired_caps import appium_desired
from time import sleep

class StarEnd(unittest.TestCase):

    def setUp(self):
        logging.info('unittest开始测试')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('测试结束')
        sleep(5)
        self.driver.close_app()


