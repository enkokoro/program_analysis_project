# Usage: ./run_test_cases.sh module
echo "Run and record tests for module named: $1"

cd examples/$1
echo "Current directory: "
pwd

# Auger
echo "Auger"
python3 -m pytest tests/auger > tests/auger/output.txt

# Deal
echo "Deal"
python3 -m pytest tests/deal > tests/deal/output.txt

# Klara
echo "Klara"
python3 -m pytest tests/klara > tests/klara/output.txt

# Pynguin
echo "Pynguin"
python3 -m pytest tests/pynguin > tests/pynguin/output.txt