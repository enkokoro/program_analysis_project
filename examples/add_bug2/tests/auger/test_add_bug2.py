import add_bug2
import unittest


class Add_bug2Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            add_bug2.add(a=1,b=3),
            4
        )


if __name__ == "__main__":
    unittest.main()
