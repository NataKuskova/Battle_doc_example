import unittest
from app.mul1 import mul


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mul(self):
        self.assertEquals(
            mul(2, 3),
            7
        )
