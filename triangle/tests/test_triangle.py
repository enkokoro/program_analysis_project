import triangle
import unittest


class TriangleTest(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(
            triangle.triangle(x=0,y=1,z=2),
            'Scalene triangle'
        )


if __name__ == "__main__":
    unittest.main()
