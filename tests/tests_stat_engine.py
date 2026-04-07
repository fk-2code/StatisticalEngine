import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        engine = StatEngine([1,2,3,4,5])
        self.assertEqual(
            engine.get_mean(),
            3
        )

    def test_median_odd(self):
        engine = StatEngine([1,2,3])
        self.assertEqual(
            engine.get_median(),
            2
        )

    def test_median_even(self):
        engine = StatEngine([1,2,3,4])
        self.assertEqual(
            engine.get_median(),
            2.5
        )

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            StatEngine([])

    def test_standard_deviation(self):
        engine = StatEngine(
            [2,4,4,4,5,5,7,9]
        )

        self.assertAlmostEqual(
            engine.get_standard_deviation(False),
            2
        )

if name == "main":
    unittest.main()
