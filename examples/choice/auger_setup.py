import auger
import choice as module
def main():
	# TODO: replace with invocation of function
	module.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
if __name__ == '__main__':
	with auger.magic([module]):
		main()