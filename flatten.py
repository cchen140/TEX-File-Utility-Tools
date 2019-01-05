#!/usr/bin/python
'''
This program is modified based on the source code provided in the following link.
http://dropbearcode.blogspot.com/2011/09/multiple-file-latex-diff.html
'''

import sys
import os
import re

inputPattern = re.compile("^(?!%).*\\\input{(.*)}")
dirpath = ""

def flattenLatex( rootFilename ):
    with open(rootFilename,'r') as fh:
        for line in fh:
            match = inputPattern.search( line )
            if match:
                newFile = match.group(1)
                if not newFile.endswith('tex'):
                    newFile += '.tex'
                flattenLatex( os.path.join(dirpath,newFile) )
            else:
                sys.stdout.write(line)

# Usage Example: python flatten.py root_main.tex > flatten_main.tex
if __name__ == "__main__":
    dirpath = os.path.split( sys.argv[1] )[0]
    flattenLatex( sys.argv[1] )
