# 使用discover 可以一次调用多个脚本
# test dir 被测试脚本的路径
# pattern 脚本名称匹配规则。

import unittest
test_dir='./'   # 要执行的脚本存放路径
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')  # 找到脚本存放路径，匹配模块名称为test开头的py文件

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)