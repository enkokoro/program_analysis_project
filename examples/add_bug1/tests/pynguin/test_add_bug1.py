# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import add_bug1 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xba#U\xa8k\x1c\x1d\xbcA\xd5\xec`3\xe6"
    module_0.add(bytes_0, bytes_0)
