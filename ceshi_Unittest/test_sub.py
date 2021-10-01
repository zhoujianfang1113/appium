from calculator import *
from StarEnd import *


class TestSub(Test_StarEnd):
    def test_sub(self):
        i=Math(3,2)
        self.assertEqual(i.sub(),1)