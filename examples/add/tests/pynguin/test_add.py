# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import add as module_0


def test_case_0():
    str_0 = "Jc}ah \r"
    var_0 = module_0.add(str_0, str_0)
    assert var_0 == "Jc}ah \rJc}ah \r"
