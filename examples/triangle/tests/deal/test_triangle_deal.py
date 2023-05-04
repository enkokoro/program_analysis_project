import deal
import triangle_deal as module

@deal.cases(module.triangle)
def test_triangle(case: deal.TestCase) -> None:
	case()