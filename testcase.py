#!/usr/bin/env python
import sys
import simplejson as json
import numpy as np
import pandas as pd


from os import chdir, getcwd, listdir
from os.path import isfile
files = []
chdir("./")

for file in listdir():
    if isfile(file):
    	if file.endswith(".ipynb") and not file.endswith("solucao.ipynb"):
        	files = files + [file]



for file in files:
    print('\n\nTestando o arquivo:', file)
    source = ''
    code = json.load(open(file))
    for cell in code['cells']:
        if cell['cell_type'] == 'code':
            for line in cell['source']:
                source = source + line
            source = source + '\n'
    exec(source)
    
    #Testando a função zscore
    Xdados2T = np.copy(Xdados2)
    Xdados2T, mean_, std_ = zscores(Xdados2T, bias=True)
    print("zscores:", Xdados2T[0:3, 1:])
    
    # Testando sua função custo
    Xdados1T = np.copy(Xdados1)
    Xdados1T, mean_, std_ = zscores(Xdados1T, bias=True)
    thetasTeste = np.array([1.0647, 0.1106])
    c = funcaoCusto(Xdados1T, Ydados1, mdados1, thetasTeste)
    print("Custo:", format(c))
    
    # Testando sua função derivadaDaFuncaoCusto
    Xdados1T = np.copy(Xdados1)
    Xdados1T, mean_, std_ = zscores(Xdados1T, bias=True)
    thetasTeste = np.array([0.827225, 0.085157])
    d = derivadaDaFuncaoCusto(Xdados1T, Ydados1, mdados1, thetasTeste)
    print("Derivada = "+format(d))
    
    #Testando a funcao predicao	
    thetasTeste = np.array([0.827225, 0.085157])
    x = np.array([1, 3.5])
    p = predicao(x, thetasTeste)
    print("Predição:", format(p))
