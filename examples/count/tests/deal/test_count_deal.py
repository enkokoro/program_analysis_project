import deal
import count_deal as module

@deal.cases(module.count)
def test_count(case: deal.TestCase) -> None:
	case()