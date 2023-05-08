import sneaky_div_types


def test_sneaky_div_0():
    assert sneaky_div_types.sneaky_div(0, -1) == 0
    assert sneaky_div_types.sneaky_div(0, 0) == 0
