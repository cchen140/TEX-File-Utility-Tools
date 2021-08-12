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


def rm_hl(filename):
    """ Remove all \\hl{} blocks in the given tex file. """

    with open(filename) as f:
        l_bracket_count = 0
        c = f.read(1)
        while c:
            if c == "\\":
                str_to_be_printed = "\\"
                while True:
                    c1 = f.read(1)
                    str_to_be_printed += c1
                    if c1 != "h":
                        break

                    c2 = f.read(1)
                    str_to_be_printed += c2
                    if c2 != "l":
                        break

                    c3 = f.read(1)
                    str_to_be_printed += c3
                    if c3 != "{":
                        break
                    else:
                        str_to_be_printed = ""
                        l_bracket_count = 1
                        break

                if len(str_to_be_printed) == 2:
                    sys.stdout.write(str_to_be_printed)
                    c = f.read(1)
                elif len(str_to_be_printed) > 2:
                    sys.stdout.write(str_to_be_printed[:-1])
                    c = str_to_be_printed[-1]
                else: # nothing to be printed
                    c = f.read(1)
                continue

            elif c == "%":
                while c != "\n":
                    sys.stdout.write(c)
                    c = f.read(1)
                sys.stdout.write(c)
                c = f.read(1)
                continue
            elif c == "{":
                if l_bracket_count > 0:
                    l_bracket_count += 1
                sys.stdout.write(c)
                c = f.read(1)
                continue
            elif c == "}":
                if l_bracket_count == 1:
                    l_bracket_count = 0
                else:
                    sys.stdout.write(c)
                    if l_bracket_count > 0:
                        l_bracket_count -= 1

                c = f.read(1)
                continue
            else:
                sys.stdout.write(c)
                c = f.read(1)
                continue


# Usage Example: python rm_hl.py source.tex > output.tex
if __name__ == "__main__":
    rm_hl(sys.argv[1])
