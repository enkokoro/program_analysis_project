# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import triangle as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.triangle(bool_0, bool_0, bool_0)
    assert var_0 == "Equilateral triangle"
    var_1 = module_0.triangle(bool_0, bool_0, bool_0)
    assert var_1 == "Equilateral triangle"
    none_type_0 = None
    var_2 = module_0.triangle(bool_0, none_type_0, none_type_0)
    assert var_2 == "Isosceles triangle"


def test_case_1():
    complex_0 = -209.52543 + 3072.84j
    tuple_0 = (complex_0,)
    var_0 = module_0.triangle(tuple_0, complex_0, tuple_0)
    assert var_0 == "Isosceles triangle"
    var_1 = module_0.triangle(tuple_0, var_0, complex_0)
    assert var_1 == "Scalene triangle"


def test_case_2():
    int_0 = -3002
    dict_0 = {int_0: int_0}
    list_0 = [dict_0, int_0, int_0]
    none_type_0 = None
    var_0 = module_0.triangle(list_0, list_0, none_type_0)
    assert var_0 == "Isosceles triangle"
