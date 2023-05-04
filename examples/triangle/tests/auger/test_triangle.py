import triangle
import unittest


class TriangleTest(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(
            triangle.triangle(x=1,y=2,z=2),
            'Isosceles triangle'
        )


if __name__ == "__main__":
    unittest.main()
