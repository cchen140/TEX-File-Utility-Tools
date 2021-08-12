"""
MIT License

Copyright (c) 2021 CY Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

L_STR = '\\begin{comment}'
R_STR = '\\end{comment}'


def rm_comments(filename):
    """ Remove all comment blocks in the given tex file. """
    with open(filename) as f:
        left_count = 0
        while True:
            line = f.readline()
            if not line:
                break

            if len(line.strip()) > 0 and line.strip()[0] == '%':
                continue

            if L_STR in line or R_STR in line:
                if L_STR in line:
                    if left_count == 0:
                        sys.stdout.write(line[:line.find(L_STR)] + '\r\n')
                    left_count += line.count(L_STR)

                if R_STR in line:
                    left_count -= line.count(R_STR)
                    if left_count == 0:
                        sys.stdout.write(line[line.rfind(R_STR)+len(R_STR):])

                continue

            if left_count > 0:
                continue

            sys.stdout.write(line)
    return 0


# Usage Example: python rm_comments.py source.tex > output.tex
if __name__ == "__main__":
    rm_comments(sys.argv[1])
