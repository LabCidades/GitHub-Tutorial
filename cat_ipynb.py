#!/usr/bin/env python
import sys
import json

from os import chdir, getcwd, listdir
from os.path import isfile
files = []

chdir("./")
print(getcwd())

for c in listdir():
    if isfile(c):
    	if c.endswith(".ipynb"):
        	print(c)



for file in files:
    print('# file: %s' % file)
    print('# vi: filetype=python')
    print('')
    code = json.load(open(file))

    for cell in code['cells']:
        if cell['cell_type'] == 'code':
            print('# -------- code --------')
            for line in cell['source']:
                print(line, end='')
            print('\n')
        elif cell['cell_type'] == 'markdown':
            print('# -------- markdown --------')
            for line in cell['source']:
                print("#", line, end='')
            print('\n')