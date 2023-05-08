import triangle
import unittest


class TriangleTest(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(
            triangle.triangle(x=3,y=4,z=5),
            'Scalene triangle'
        )


if __name__ == "__main__":
    unittest.main()
