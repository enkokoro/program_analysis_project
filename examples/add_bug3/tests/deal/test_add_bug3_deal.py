import deal
import add_bug3_deal as module

@deal.cases(module.add)
def test_add_bug3(case: deal.TestCase) -> None:
	case()