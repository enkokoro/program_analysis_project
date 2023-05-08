import deal
import uninterpretable_types as module

@deal.cases(module.uninterpretable)
def test_uninterpretable(case: deal.TestCase) -> None:
	case()