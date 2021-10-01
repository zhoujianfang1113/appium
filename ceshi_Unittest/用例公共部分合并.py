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
        j=Math(5,5)
        self.assertEqual(j.add(),10)
class TestSub(Test_StarEnd):
    def test_sub(self):
        i=Math(3,2)
        self.assertEqual(i.sub(),1)


if __name__ == '__main__':
    # unittest.main()   # 运行上面的所有用例。

    # 运行上面的单个用例
    suite=unittest.TestSuite()
    suite.addTest(Testadd('test_add'))
    suite.addTest(TestSub('test_sub'))
    unittest.TextTestRunner().run(suite)   # 执行用例

