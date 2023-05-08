import deal
import add_types as module

@deal.cases(module.add)
def test_add(case: deal.TestCase) -> None:
	case()