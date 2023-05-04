import deal
import triangle as module

@deal.cases(module.triangle)
def test_triangle(case: deal.TestCase) -> None:
    case()