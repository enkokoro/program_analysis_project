import deal
import uninterpretable_deal as module

@deal.cases(module.uninterpretable)
def test_uninterpretable(case: deal.TestCase) -> None:
	case()