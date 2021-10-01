from calculator import *
from StarEnd import *

class Testadd(Test_StarEnd):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)