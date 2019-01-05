#!/usr/bin/python
import sys


def removeHightlight( filename ):
    with open(filename) as f:
        inHlLeftBracketCount = 0
        c = f.read(1)
        while c:
            if c == "\\":
                toBePrinted = "\\"
                while True:
                    c1 = f.read(1)
                    toBePrinted += c1
                    if c1 != "h":
                        break

                    c2 = f.read(1)
                    toBePrinted += c2
                    if c2 != "l":
                        break

                    c3 = f.read(1)
                    toBePrinted += c3
                    if c3 != "{":
                        break
                    else:
                        toBePrinted = ""
                        inHlLeftBracketCount = 1
                        break

                if len(toBePrinted) == 2:
                    sys.stdout.write(toBePrinted)
                    c = f.read(1)
                elif len(toBePrinted) > 2:
                    sys.stdout.write(toBePrinted[:-1])
                    c = toBePrinted[-1]
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
                if inHlLeftBracketCount > 0:
                    inHlLeftBracketCount += 1
                sys.stdout.write(c)
                c = f.read(1)
                continue
            elif c == "}":
                if inHlLeftBracketCount == 1:
                    inHlLeftBracketCount = 0
                else:
                    sys.stdout.write(c)
                    if inHlLeftBracketCount > 0:
                        inHlLeftBracketCount -= 1

                c = f.read(1)
                continue
            else:
                sys.stdout.write(c)
                c = f.read(1)
                continue


# Usage Example: python removehl.py source.tex > output.tex
if __name__ == "__main__":
    removeHightlight( sys.argv[1] )
