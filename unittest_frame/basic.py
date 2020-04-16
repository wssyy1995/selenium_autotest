# 使用unittest测试框架

#1：导入unittesti
import unittest
#2.导入要测试的


#3：创建一个要测试类，继承unittest.TestCase(一个测试类相当于一个功能的测试用例的合集)
class CountTest(unittest.TestCase):

    #setUp为初始化方法，每一个test*方法运行前后都会执行setUp和tearDown,可以放入每个方法的通用步骤;
    def setUp(self):
        print('test start')

    #4:创建一个测试方法，需要以test开头（一般一条测试方法为一条测试用例）
    def test_add(self):
        ret=15
        print('test_add')

        #6：断言：self.assertEqual(实际结果，预期结果)
        self.assertEqual(ret,15,msg='result is wrong')
    '''
        其他断言：
         -assertNotEqual(a.b)
         -assertTrue(x)
         -assertIn(a,b)
         -assertIn(a,b)        
    '''
    def test_add2(self):
        ret=888885
        print('test_add2')
        self.assertEqual(ret, 888885,msg='result is wrong')

    #善后方法，清除测试过程中产生的数据
    def tearDown(self):
        print('test end')



if __name__ =='__main__':
    # 7.运行
    #方法一.运行所有包含在该模块中以'test'命名开头的测试方法
    unittest.main()
    # 注意，main()的方式执行测试方法时，不是按照测试用例的从上往下的顺序，而是按照测试方法名的ASCII码的顺序；如果一定要按照某个顺序，需要用TestSuite类的addTest()方法

    #方法二.当不想执行所有测试用例时：
    # #1.构造测试集
    # suite=unittest.TestSuite()
    # suite.addTest(测试类名('测试方法名'))
    # #2.执行测试集的测试
    # runner=unittest.TextTestRunner()
    # runner.run(suite)




