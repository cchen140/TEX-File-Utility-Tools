### TEX File Utility Tools

Tools in this repository are initially developed for processing latex files to be fed into `latexdiff`.

To use them, run `flatten.py` first and then `rm_hl.py` or `rm_comments.py`
based on your needs before feeding the output tex file into `latexdiff`.   

---
#### flatten.py
Expand all `\input{}` in the given tex file, recursively.

Example: `python flatten.py src.tex > dst.tex`

#### rm_hl.py
Remove all \\hl{} blocks in the given tex file.

Example: `python rm_hl.py src.tex > dst.tex`


#### rm_comments.py
Remove all comment blocks in the given tex file.

Example: `python rm_comments.py src.tex > dst.tex`
