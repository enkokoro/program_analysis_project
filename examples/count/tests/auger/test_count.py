import count
import unittest


class CountTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(
            count.count(items=[1, 2, 3, 4, 2, 3, 4, 3, 4, 4],item=3),
            3
        )


if __name__ == "__main__":
    unittest.main()
