import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([5,5,5]), 15)
        self.assertEqual(sum([5,5,6]), 16)
        self.assertEqual(sum([10,10,10]), 30)
        self.assertEqual(sum([20,10,10]), 40)
        self.assertEqual(max(30, 50, 20), 50)

if __name__ == '__main__':
    unittest.main()