import auger
import count as module
def main():
	# TODO: replace with invocation of function
	module.count([1, 2, 3, 4, 2, 3, 4, 3, 4, 4], 3)
if __name__ == '__main__':
	with auger.magic([module]):
		main()