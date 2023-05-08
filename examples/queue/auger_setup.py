import auger
import queue as module
def main():
	# TODO: replace with invocation of function
	q = module.Queue(5)
	print(q.empty())
	print(q.full())
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())

if __name__ == '__main__':
	with auger.magic([module]):
		main()