import deal
import add_bug1_types as module

@deal.cases(module.add)
def test_add_bug1(case: deal.TestCase) -> None:
	case()