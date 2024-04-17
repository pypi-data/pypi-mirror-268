import unittest
from confidence_interval.core import mean_confidence_interval

class TestMeanCI(unittest.TestCase):
    def test_mean_confidence_interval(self):
        data = [1, 2, 3, 4, 5]
        mean, lower, upper = mean_confidence_interval(data)
        self.assertAlmostEqual(mean, 3.0)
        # Add more assertions for lower and upper

if __name__ == '__main__':
    unittest.main()
