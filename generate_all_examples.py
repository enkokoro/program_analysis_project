import os
import sys
def setup():
    example_tests = os.listdir("examples")
    for test_name in example_tests:
        print(f"Generating tests for: {test_name}")
        os.system(f"python3 generate_tests.py --module-name={test_name}")
        print("="*80)
def auger_setup():
    example_tests = os.listdir("examples")
    for test_name in example_tests:
        print(f"Generating auger tests for: {test_name}")
        os.system(f"python3 generate_tests.py --auger={test_name}")
        print("="*80)

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "--setup":
        setup()
    elif args[0] == "--auger":
        auger_setup()
    else:
        print("Invalid falg, only accepts --setup or --auger")