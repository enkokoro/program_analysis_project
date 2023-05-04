import os
import sys

def example_directory(test_name):
    return f"examples/{test_name}"
def example_file(test_name):
    return f"{example_directory(test_name)}/{test_name}.py"
def example_types_file(test_name):
    return f"{example_directory(test_name)}/{test_name}_types.py"
def test_directory(test_name):
    return f"{example_directory(test_name)}/tests"
def make_tool_directory(test_name, tool):
    tool_dir = f"{test_directory(test_name)}/{tool}"
    if not os.path.exists(tool_dir):
        os.mkdir(tool_dir)
    return tool_dir


def directory_check(test_name):
    # run from base project folder
    return (os.path.isdir(example_directory(test_name)) 
            and os.path.exists(example_file(test_name))
            and os.path.exists(example_types_file(test_name)))
    
def directory_explanation(test_name):
    explanation = "In the 'examples' directory, please have a folder corresponding to the test with the following structure"
    structure = f"{test_name}/\n|- {test_name}.py: base version of file that you want to generate test cases for\n|- triangle_{types}.py: modified versions annotated with types"
    return explanation + structure

def directory_setup(test_name):
    # run from base project folder
    test_dir = test_directory(test_name)
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)

def pynguin_setup(test_name):
    # run from base project folder
    os.system("export PYNGUIN_DANGER_AWARE=true")
    pynguin_dir = make_tool_directory(test_name, "pynguin")
    # create base test version
    print("Generating pynguin tests...")
    os.system(f"pynguin --project-path {example_directory(test_name)} --output-path {pynguin_dir} --module-name {test_name}")
    # create types test version
    os.system(f"pynguin --project-path {example_directory(test_name)} --output-path {pynguin_dir} --module-name {test_name}_types")
    print("done.")

def klara_setup(test_name):
    klara_dir = make_tool_directory(test_name, "klara")
    print("Generating klara tests...")
    os.system(f"klara {example_file(test_name)}")
    os.rename(f"test_{test_name}.py", f"{klara_dir}/test_{test_name}.py")
    os.system(f"klara {example_types_file(test_name)}")
    os.rename(f"test_{test_name}_types.py", f"{klara_dir}/test_{test_name}_types.py")
    print("done.")

def deal_setup(test_name):
    deal_dir = make_tool_directory(test_name, "deal")
    print("Generating deal test setup...")
    for tn in [f"{test_name}_types", f"{test_name}_deal"]:
        deal_file = ["import deal",
                    f"import {tn} as module",
                    "",
                    f"@deal.cases(module.{test_name})",
                    f"def test_{test_name}(case: deal.TestCase) -> None:",
                    "\tcase()"]
        deal_file = "\n".join(deal_file)
        deal_filename = f"{deal_dir}/test_{tn}.py"
        with open(deal_filename, "w") as file:
            file.write(deal_file)
    print("done.")

def auger_setup(test_name):
    auger_dir = make_tool_directory(test_name, "auger")
    print("Generating auger test setup...")
    auger_file = ["import auger",
                  f"import {test_name} as module",
                  "def main():",
                  "\t# TODO: replace with invocation of function",
                  "if __name__ == '__main__':",
                  "\twith auger.magic([module]):",
                  "\t\tmain()"]
    auger_file = "\n".join(auger_file)
    auger_setup_filename = f"{example_directory(test_name)}/auger_setup.py"
    with open(auger_setup_filename, "w") as file:
        file.write(auger_file)
    print(f"done, but AUGER requires additional programmer input, check {auger_setup_filename}.")

def auger_run(test_name):
    os.chdir(example_directory(test_name))
    os.system("python3 auger_setup.py")
    os.rename(f"tests/test_{test_name}.py", f"tests/auger/test_{test_name}.py")

def main():
    args = sys.argv[1:]
    prefix = "--module-name="
    auger_prefix = "--auger="
    if len(args) != 1 or (args[0][:len(prefix)] != prefix and args[0][:len(auger_prefix)] != auger_prefix):
        print("Usage: python3 generate_tests.py --module-name=example_name")
        print("Or: python3 generate_tests.py --auger=example_name")
        return 
    if args[0][:len(prefix)] == prefix:
        test_name = args[0][len(prefix):]
        if not directory_check(test_name):
            print("Directory not set up properly, make sure you are running from project root folder and have correct setup.")
            print(directory_explanation(test_name))
            return 
        
        directory_setup(test_name)
        pynguin_setup(test_name)
        klara_setup(test_name)
        deal_setup(test_name)
        auger_setup(test_name)
    elif args[0][:len(auger_prefix)] == auger_prefix:
        test_name = args[0][len(auger_prefix):]
        auger_run(test_name)

if __name__=="__main__":
    main()
    
