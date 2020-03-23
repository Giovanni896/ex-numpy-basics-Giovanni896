import unittest
from main import uniform, gaussian


class TestCase(unittest.TestCase):
    def test_uniform(self):
        x = uniform(10000, 1000)
        self.assertEqual(x.shape[0], 10000)
        self.assertEqual(x.shape[1], 1000)
        self.assertAlmostEqual(x.mean(), 0.5, delta=1e-3)

    def test_gaussian(self):
        x = gaussian(10000, 1000)
        avg = x.mean()
        std = x.std()
        self.assertEqual(x.shape[0], 10000)
        self.assertEqual(x.shape[1], 1000)
        self.assertAlmostEqual(avg, 0, delta=1e-3)
        self.assertAlmostEqual(std, 1, delta=1e-3)


if __name__ == '__main__':
    unittest.main()
