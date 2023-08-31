#!/bin/bash

ROOT="/MoneyLikeGold"

files=$(find "$ROOT" -name "*.py")

for file in $files
do
    echo "Running pycodestyle on $file"
    pycodestyle "$file"
done
