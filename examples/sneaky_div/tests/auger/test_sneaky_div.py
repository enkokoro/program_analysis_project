import sneaky_div
import unittest


class Sneaky_divTest(unittest.TestCase):
    def test_sneaky_div(self):
        self.assertEqual(
            sneaky_div.sneaky_div(v1=1,v2=2),
            2
        )


if __name__ == "__main__":
    unittest.main()
