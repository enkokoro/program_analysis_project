import auger
import triangle as module
def main():
	# TODO: replace with invocation of function
	module.triangle(3, 4, 5)
if __name__ == '__main__':
	with auger.magic([module]):
		main()