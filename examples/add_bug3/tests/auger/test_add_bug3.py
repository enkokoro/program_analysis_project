import add_bug3
import unittest


class Add_bug3Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            add_bug3.add(a=1,b=3),
            4
        )


if __name__ == "__main__":
    unittest.main()
