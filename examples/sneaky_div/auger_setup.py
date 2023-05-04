import auger
import sneaky_div as module
def main():
	# TODO: replace with invocation of function
	module.sneaky_div(1, 2)
if __name__ == '__main__':
	with auger.magic([module]):
		main()