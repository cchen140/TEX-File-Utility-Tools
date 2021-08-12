#!/bin/bash

# Assuming:
# original root tex file at: "org/main.tex"
# new root tex file at:      "curr/main.tex"
# output tex file at:        "curr/diff_main.tex"

python flatten.py org/main.tex > org/flatten_main.tex
python rm_hl.py org/flatten_main.tex > org/nonhl_main.tex
python rm_comments.py org/nonhl_main.tex > org/nonhlcm_main.tex

python flatten.py curr/main.tex > curr/flatten_main.tex
python rm_hl.py curr/flatten_main.tex > curr/nonhl_main.tex
python rm_comments.py curr/nonhl_main.tex > curr/nonhlcm_main.tex

latexdiff org/nonhlcm_main.tex curr/nonhlcm_main.tex > curr/diff_main.tex

