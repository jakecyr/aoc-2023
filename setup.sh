TEMPLATE=$(cat template.py)

if [ -z "$1" ]
  then
    echo "Please provide a day number"
    exit 1
fi

touch aoc/day_$1.py
touch tests/test_day_$1.py
touch inputs/day_$1.txt

echo "$TEMPLATE" > aoc/day_$1.py
echo "from aoc import day_$1" > tests/test_day_$1.py

code aoc/day_$1.py
code tests/test_day_$1.py
