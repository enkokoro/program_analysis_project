# List of Tools
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
- annotate file
- python3 -m pytest tests/deal

TSTL: https://github.com/agroce/tstl
- pip install tstl
- tstl tests/tstl/triangle.tstl
- tstl_rt --timeout 30 
- [having trouble figuring out how to work]

CrossHair: https://crosshair.readthedocs.io/en/latest/get_started.html
- pip install crosshair-tool
- crosshair watch [directory with code to analyze]
- [having trouble figuring out how to work]

Klara: https://klara-py.readthedocs.io/en/latest/introduction.html
- pip install klara
- klara source.py

Auger: https://github.com/laffra/auger
- pip install auger-python
- python3 auger_setup.py

# Comments from project proposal
Two key questions I have for you to think about/contend with: (1) which shared programs do you want to test (and why are they good, or how should you pick them)? and (2) what metrics are you using to compare test generation tools or techniques?

# Steps to run
1. Create virtual environment with requirements.txt and use it
    from within the final project directory
        python -m venv venv (or whatever path desired)
        source venv/bin/activate
2. 

# Structure of example
triangle/
|- triangle.py: base version of file that you want to generate test cases for
|- triangle_*.py: modified versions to work with different tools
|- tests/
    |- test_triangle.py: test cases