import deal
import count_types as module

@deal.cases(module.count)
def test_count(case: deal.TestCase) -> None:
	case()