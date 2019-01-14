#!/bin/bash

python flatten.py curr/main.tex > curr/flatten_main.tex
python removehl.py curr/flatten_main.tex > curr/nonhl_main.tex
latexdiff org/flatten_main.tex curr/nonhl_main.tex > curr/diff_main.tex
