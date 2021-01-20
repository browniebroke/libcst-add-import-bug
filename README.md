# libCST add import bug demo

This is demo repo showing the problem reported in https://github.com/Instagram/LibCST/issues/447

## Content

Here is how this repo is divided:

- `codemods/`: a very basic codemodder to run
- `src/`: the code to be transformed by the provided codemodder

## How to reproduce the problem

1. Create a virtualenv
2. Install the dependencies `pip install -r requirements.txt`
3. Run the provided codemodder: `python3 -m libcst.tool codemod demo.DemoCommand src`

## Problem

* *Expected:* the import `from codemod.has import run` should be added to `src/example.py` only.
* *Actual:* the import is also added to `src/orther.py`.
