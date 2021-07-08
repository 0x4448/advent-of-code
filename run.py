#!/usr/bin/env python3

# Compute the answer when given a module, callable, and input.

import argparse
import importlib
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("module", type=str)
parser.add_argument("callable", type=str)
parser.add_argument("input", type=pathlib.Path)
args = parser.parse_args()

mod = importlib.import_module(args.module)

with open(args.input) as fp:
    data = fp.read()

print(getattr(mod, args.callable)(data))
