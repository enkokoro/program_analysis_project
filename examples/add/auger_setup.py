import auger
import add as module
def main():
	# TODO: replace with invocation of function
	module.add(1, 3)
if __name__ == '__main__':
	with auger.magic([module]):
		main()