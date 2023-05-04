import triangle_types


def test_triangle_0():
    assert triangle_types.triangle(0, 0, 0) == 'Equilateral triangle'
    assert triangle_types.triangle(1, 0, 0) == 'Isosceles triangle'
    assert triangle_types.triangle(2, 0, 1) == 'Scalene triangle'
