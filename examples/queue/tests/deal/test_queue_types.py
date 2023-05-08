import deal
import queue_types as module

@deal.cases(module.queue)
def test_queue(case: deal.TestCase) -> None:
	case()