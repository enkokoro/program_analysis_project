# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import add_bug3_types as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.add(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -17
    int_1 = module_0.add(int_0, int_0)
    assert int_1 == -34
    none_type_0 = None
    int_2 = module_0.add(int_1, int_1)
    module_0.add(int_0, none_type_0)
