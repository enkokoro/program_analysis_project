import add as module
import unittest


class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            module.add(a=1,b=3),
            4
        )


if __name__ == "__main__":
    unittest.main()
