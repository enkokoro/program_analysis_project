import uninterpretable
import unittest


class UninterpretableTest(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(
            uninterpretable.foo(v1=3),
            3
        )


if __name__ == "__main__":
    unittest.main()
