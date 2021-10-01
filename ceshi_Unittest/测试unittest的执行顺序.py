# setup与tearDown 是公共的，每次使用时都要调用。

from calculator import *
import unittest

class Test_StarEnd(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('测试结束')


# 继承上面的公共类,在class后面的括号内写入。
class Testadd(Test_StarEnd):
    def test_add(self):
        print('我是1')
class TestSub(Test_StarEnd):
    def test_sub(self):
        print('我是2')


if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestSub('test_sub'))
    suite.addTest(Testadd('test_add'))
    unittest.TextTestRunner().run(suite)   # 执行用例

