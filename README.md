# List of Automatic Test Generation Tools
pynguin: https://pynguin.readthedocs.io/en/latest/user/quickstart.html 
- pip install pynguin
- pynguin \
    --project-path ./docs/source/_static \
    --output-path /tmp/pynguin-results \
    --module-name example 
- requires environment variable PYNGUIN_DANGER_AWARE set to continue - run in container for safety unless you know that the code you run is safe (export PYNGUIN_DANGER_AWARE=true)
- python3 -m pytest tests/pynguin

deal: https://deal.readthedocs.io/details/examples.html
- python3 -m pip install --user 'deal[all]'
- annotate file with deal contracts
- python3 -m pytest tests/deal

~~TSTL: https://github.com/agroce/tstl~~
- pip install tstl
- tstl tests/tstl/triangle.tstl
- tstl_rt --timeout 30 
- [having trouble figuring out how to work]

~~CrossHair: https://crosshair.readthedocs.io/en/latest/get_started.html~~
- pip install crosshair-tool
- crosshair watch [directory with code to analyze]
- [having trouble figuring out how to work]

Klara: https://klara-py.readthedocs.io/en/latest/introduction.html
- pip install klara
- klara source.py

Auger: https://github.com/laffra/auger
- pip install auger-python
- annotate file to run main in auger.magic
- python3 python_file.py

# Steps to run
1. Create virtual environment with requirements.txt and use it from within the final project directory
        
    ``python -m venv venv`` (or whatever path desired)
        
    ``source venv/bin/activate``

    ``python3 -m pip install -r requirements.txt``
2. Set environment variable for Pynguin to work. Setting this environment variable acknowledges that Pynguin will run any of the source code provided, which may bring harm to your computer if the code is not safe.
    ``export PYNGUIN_DANGER_AWARE=true``
3. Create example module in examples folder following the structure

    ```
    project/
    │   README.md 
    └───examples/
    |   └───module/
    │       │   module.py: base version of file that you want to generate test cases for
    │       │   module_types.py: type annotated version
    |       |   module_deal.py: deal annotated version
    │       └───tests/
    │           └─── (tool)/: subfolders corresponding to each tool (will be created by script for you)
    │                 │       test_module.py: generated or created test files from the tool it belongs to (will be created by script for you)
    ```
    for an example of a type annotated version, see ``examples/add/add_types.py`` and for an example of a deal annotated version, see ``examples/add/add_deal.py``

4. To generate test functions for all examples and the setup for the auger test file, run

    ``python3 generate_all_examples.py --setup``

    Alternatively, run the following from the project root directory for the setup for one module in the examples folder, substituting ``foo`` for the desired module name 

    ``python3 generate_tests.py --module-name=foo``

    NOTE: Auger and Deal may require additional setup. 
    
    DEAL: The deal test file found at ``examples/foo/tests/test_foo_deal.py`` assumes the function that you want to test has the same name as the module by annotating the test function with ``@deal.cases(module.foo)``. To override this, change ``foo`` to the desired function and add additional test functions if necessary.

    AUGER: Auger requires the invokation of a main function. The auger setup file can be found at ``examples/foo/auger_setup.py``, add code under the commeng ``# TODO: replace with invocation of function``. Then, to actually generate the auger testfile, the setup file must be run.

    To do so, run the following to run all auger setup files from the project root directory

    ``python3 generate_all_examples.py --auger``

    or run the following for a specific module from the project root directory

    ``python3 generate_tests.py --auger=foo``

    The test files can then be found at ``examples/foo/tests`` and are grouped in directories corresponding to the test generation tool.

5. To run a test file, enter the corresponding directory, for example ``examples/foo`` and then run ``python3 -m pytest tests/tool`` to run the tests corresponding to the tool. To run all the test files and create an output text file, use the script ``run_test_cases.sh``. For example to run test cases for a module named ``foo``:

    ``chmod +x run_test_cases.sh``

    ``./run_test_cases.sh foo``



