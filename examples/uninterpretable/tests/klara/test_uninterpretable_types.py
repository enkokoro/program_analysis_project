import uninterpretable_types


def test_foo_0():
    assert uninterpretable_types.foo(3) == 3
    assert uninterpretable_types.foo(0) is not None
