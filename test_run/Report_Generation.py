import unittest
from BSTestRunner import BSTestRunner
import time
import logging
import sys

# 该代码只在.bat下起作用，防止bat文件找不到路径
path=r'D:\\A_Appium_Script\\Library\\'   # 脚本存放的根目录
sys.path.append(path)

# 指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir ='../reports'

# 加载测试用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='login_unit_test.py')    # pattern 填写需要被测试的用例，如果想写多个则可以'test*.py'匹配所有test开头的.py文件。

# 定义报告的文件格式
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'    # 生成测试报告的文件名格式

# 运行用例并生成测试报告
with open(report_name,'wb')as f:
    runner=BSTestRunner(stream=f,title='藏书馆测试报告',description='藏书馆安卓APP测试报告')
    logging.info('开始跑测试用例')
    runner.run(discover)


