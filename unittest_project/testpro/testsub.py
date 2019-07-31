import unittest
from unittest_project.calculator import Count


class Testsub(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_sub(self):
        count = Count(10, 5)
        ret=count.sub()

        self.assertEqual(ret,5)

    def test_sub2(self):
        count = Count(-888880, 5)
        ret = count.sub()
        self.assertEqual(ret, -888885,msg='result is wrong')


    def tearDown(self):
        print('test end')