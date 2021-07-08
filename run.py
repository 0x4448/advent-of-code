#!/usr/bin/env python3

# Compute the answer when given a module, callable, and input.
#
# Test one input:
# ./run.py 2015.day02 get_area --input "2x3x4"
#
# Test all inputs:
# ./run.py 2015.day02 get_area --input-file 2015/inputs/day02.txt

import argparse
import importlib
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("module", type=str)
parser.add_argument("callable", type=str)
parser.add_argument("--input", type=str)
parser.add_argument("--input-file", type=pathlib.Path)
args = parser.parse_args()

mod = importlib.import_module(args.module)

if args.input:
    data = args.input
elif args.input_file:
    with open(args.input_file) as fp:
        data = fp.read()

print(getattr(mod, args.callable)(data))
