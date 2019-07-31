import unittest
from unittest_project.calculator import Count


class Testadd(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_add(self):
        count = Count(10, 5)
        ret=count.add()

        self.assertEqual(ret,15)

    def test_add2(self):
        count = Count(-888880, -5)
        ret = count.add()
        self.assertEqual(ret, -888885,msg='result is wrong')


    def tearDown(self):
        print('test end')



