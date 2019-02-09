import unittest
from calculator import add, sub, multi, div


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('sutupclass')
        cls.a = [6, 1, 10]
        cls.b = [3, 2, 5]


    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
        cls.a = []
        cls.b = []


    def setUp(self):
        print('setup')


    def tearDown(self):
        print('teardown')


    def test_add(self):
        print('test add')
        for aa, bb in zip(self.a, self.b):
            self.assertEqual(add(aa, bb), aa + bb)


    def test_sub(self):
        print('test sub')
        for aa, bb in zip(self.a, self.b):
            self.assertEqual(sub(aa, bb), aa - bb)


    def test_multi(self):
        print('test multi')
        self.assertEqual(multi(6, 3), 18)
        self.assertEqual(multi(1, 2), 2)
        self.assertEqual(multi(10, 5), 50)


    def test_div(self):
        print('test div')
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(1, 2), 0.5)
        self.assertEqual(div(10, 5), 2)
        with self.assertRaises(ZeroDivisionError):
            div(3, 0)
    

    def test_etc(self):
        print('test etc')
        self.assertEqual([1, 2, 3, 4], [1, 2, 3, 4])
        self.assertFalse(False)
        self.assertGreater(6, 5)


unittest.main()
