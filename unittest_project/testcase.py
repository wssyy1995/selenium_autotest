

#1：导入unittesti
import unittest
#2.导入要测试的函数
from calculator import Count,is_prime


#3：创建一个要测试这个函数的类，继承unittest.TestCase
class CountTest(unittest.TestCase):

    #setUp为初始化方法，可以放入每个方法的通用步骤
    def setUp(self):
        print('test start')

    #4:创建一个方法，一般这个方法为一条测试用例
    def test_add(self):
        count = Count(10, 5)
        ret=count.add()

        #6：断言：self.assertEqual(实际结果，预期结果)
        self.assertEqual(ret,15)

    def test_add2(self):
        count = Count(-888880, -5)
        ret = count.add()
        self.assertEqual(ret, -888885,msg='result is wrong')

    def test_sub(self):
        count = Count(1,5)
        ret = count.sub()
        self.assertEqual(ret, -4)

    def test_sub2(self):
        count = Count(9,5)
        ret = count.sub()
        self.assertEqual(ret, 4)

    #善后方法，清除测试过程中产生的数据
    def tearDown(self):
        print('test end')

class PrimeTest(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_prime(self):
        self.assertTrue(is_prime(11),msg='this is not a prime')

    def test_prime2(self):
        self.assertTrue(is_prime(1), msg='this is not a prime')

    def tearDown(self):
        print('test end')



if __name__ =='__main__':
    #运行所有包含在该模块中以'test'命名开头的测试方法
    #unittest.main()

    #当不想执行所有测试用例时：
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(PrimeTest('test_prime'))
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

