import add_bug1
import unittest


class Add_bug1Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            add_bug1.add(a=1,b=3),
            -2
        )


if __name__ == "__main__":
    unittest.main()
