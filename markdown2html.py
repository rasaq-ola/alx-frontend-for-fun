#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Just for Task 0, simply copying the content (you'll extend this in future tasks)
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write(infile.read())

sys.exit(0)
