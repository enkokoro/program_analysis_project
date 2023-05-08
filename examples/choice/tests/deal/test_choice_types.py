import deal
import choice_types as module

@deal.cases(module.choice)
def test_choice(case: deal.TestCase) -> None:
	case()