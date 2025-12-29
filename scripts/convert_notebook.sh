#!/bin/bash
jupyter nbconvert --to html "notebooks/Acute Coronary Syndrome Drug Discovery Analysis.ipynb" --output-dir=docs --output=index
echo "Notebook converted to HTML successfully!"