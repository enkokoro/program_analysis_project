import deal
import add_deal as module

@deal.cases(module.add)
def test_add(case: deal.TestCase) -> None:
	case()