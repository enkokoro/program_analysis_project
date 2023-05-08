import deal
import add_bug2_deal as module

@deal.cases(module.add)
def test_add_bug2(case: deal.TestCase) -> None:
	case()