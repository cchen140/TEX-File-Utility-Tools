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

import sys, os, re


def flatten_tex_files(root_file_path, dir_path):
    """ Expand all \\input{} in the given tex file, recursively. """

    with open(root_file_path, 'r') as f:
        for line in f:
            match = re.compile("^(?!%).*\\\input{(.*)}").search(line)
            if match:
                input_file_path = match.group(1)
                if os.path.splitext(input_file_path)[1] != '.tex':
                    input_file_path += '.tex'
                flatten_tex_files(os.path.join(dir_path, input_file_path), dir_path)
            else:
                sys.stdout.write(line)


if __name__ == "__main__":
    root_tex_file_path = sys.argv[1]
    root_dir_path = os.path.dirname(root_tex_file_path)
    flatten_tex_files(root_tex_file_path, root_dir_path)
