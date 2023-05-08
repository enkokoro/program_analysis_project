import deal
import sneaky_div_types as module

@deal.cases(module.sneaky_div)
def test_sneaky_div(case: deal.TestCase) -> None:
	case()