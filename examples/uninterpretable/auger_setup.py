import auger
import uninterpretable as module
def main():
	# TODO: replace with invocation of function
	module.foo(3)
if __name__ == '__main__':
	with auger.magic([module]):
		main()