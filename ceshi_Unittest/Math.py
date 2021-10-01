from ceshi_Unittest.calculator import Math
import unittest

# 定义一个TestMath类。
class TestMath(unittest.TestCase):
# setUp（系统内置） 测试执行之前的环境准备，测试开始之前的一些链接和一些配置都可以写在这里面。
    def setUp(self):
        print("开始测试")

# test_add 自己定义的一个方法
    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)  # assertEqual 断言方法

    def test_add1(self):
        j=Math(5,10)
        self.assertTrue(j.add()>10)

    def test_add2(self):
        # j=Math(5,10)
        self.assertIn('请重新登录','您的账号已被登出请重新登录')

    def test_add3(self):
        self.assertIs('请重新登录','请重新登录')

# tearDown（系统内置） 这里面写测试完成后的一些收尾工作。（比如关闭数据库，关闭APP之类）
    def tearDown(self):
        print('测试结束')


class testSub(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def test_sub(self):
        i=Math(10,5)
        self.assertEqual(i.sub(),5)

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    # 构造测试集
    suite=unittest.TestSuite()  # 测试用例集，定义一个suite；unittest.TestSuite()是方法。
    suite.addTest(TestMath('test_add'))   # suite.addTest 调用方法，具体调用哪个方法，直接写在（）里。则（TestMath类下的test_add方法）
    suite.addTest(TestMath('test_add1'))   # suite.addTest 调用方法，具体调用哪个方法，直接写在（）里。则（TestMath类下的test_add方法）
    suite.addTest(TestMath('test_add2'))   # suite.addTest 调用方法，具体调用哪个方法，直接写在（）里。则（TestMath类下的test_add方法）
    suite.addTest(testSub('test_sub'))   # suite.addTest 调用方法，具体调用哪个方法，直接写在（）里。则（TestMath类下的test_add方法）

    # 执行测试
    unittest.TextTestRunner().run(suite)
