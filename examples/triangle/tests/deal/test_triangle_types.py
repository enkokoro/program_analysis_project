import deal
import triangle_types as module

@deal.cases(module.triangle)
def test_triangle(case: deal.TestCase) -> None:
	case()