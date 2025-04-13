#!/bin/bash

# Check if the number of tests was passed
if [ -z "$1" ]; then
  echo "Usage: $0 <number_of_tests>"
  exit 1
fi

# Loop through all tests from 1 to N
for ((i=1; i<=$1; i++))
do
  echo "[$i]"
  cat "tests/$i.pas" | python3 ana_sin.py
done
