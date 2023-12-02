TEMPLATE=$(cat template.py)

if [ -z "$1" ]
  then
    echo "Please provide a day number"
    exit 1
fi

touch aoc/day_$1.py
touch tests/test_day_$1.py

echo "$TEMPLATE" > aoc/day_$1.py
echo "from aoc import day_$1" > tests/test_day_$1.py
