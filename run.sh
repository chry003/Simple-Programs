#!/bin/bash

files=$(ls -d *)

for file in $files;
do
    echo $file
    python -m pyflowchart --no-simplify --conds-align $file/$file.py > $file/$file.flowchart
done
