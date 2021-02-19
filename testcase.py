#!/usr/bin/env python
import sys
import simplejson as json
import numpy as np
import pandas as pd
import pytest
import math

from os import chdir, getcwd, listdir
from os.path import isfile
sources = []
chdir("./")
file = "Exercicios_Regressao_Linear.ipynb"

def get_source(file):
    print('\n\nTestando o arquivo:', file)
    source = ''
    code = json.load(open(file))
    for cell in code['cells']:
        if cell['cell_type'] == 'code':
            for line in cell['source']:
                source = source + line
            source = source + '\n'
    return source
     

exec( get_source(file), globals(), locals() )
 
 
def zscore_true(X, mean=None, std=None, bias=False):    
    if bias == True:
        init = 1
    else:
        init = 0        
    if mean is None:
        mean = np.mean(X[:, init:], axis=0) 
    if std is None:
        std = np.std(X[:, init:], axis=0) 
    X[:, init:]=(X[:, init:]-mean)/(std)
    
    return (X, mean, std) 
  
  
def test_zscore():    	
    Xdados2T = np.copy(Xdados2)
    Xdados2T, mean_, std_ = zscore(Xdados2T, bias=True)
    m = np.size(Xdados2, 0)    

    Xdados_true = np.copy(Xdados2)
    Xdados_true, mean_true, std_true = zscore_true(Xdados_true, bias=True)
    #Testando a função zscore        
        
    np.testing.assert_array_equal(mean_true, mean_)
    np.testing.assert_array_equal(std_true, std_)
    np.testing.assert_array_equal(Xdados_true, Xdados2T)
        
def test_funcaoCusto():
      # Testando sua função custo
    Xdados1T = np.copy(Xdados1)
    Xdados1T, mean_, std_ = zscore_true(Xdados1T, bias=True)
    thetasTeste = np.array([1.0647, 0.1106])
    c = funcaoCusto(Xdados1T, Ydados1, mdados1, thetasTeste)
    assert abs(0.0009836391913337376 - c) < 0.000000001

def test_derivadaDaFuncaoCusto():    
    
    # Testando sua função derivadaDaFuncaoCusto
    Xdados1T = np.copy(Xdados1)
    Xdados1T, mean_, std_ = zscore_true(Xdados1T, bias=True)
    thetasTeste = np.array([0.827225, 0.085157])
    d = derivadaDaFuncaoCusto(Xdados1T, Ydados1, mdados1, thetasTeste)
    d_true = np.array([-0.237455, -0.02430041])
    #print(abs(d[0] - d_true[0]))
    assert abs(d[0] - d_true[0]) < 0.0001 and abs(d[1] - d_true[1]) < 0.0001
    
def test_predicao():    
    #Testando a funcao predicao	
    thetasTeste = np.array([0.827225, 0.085157])
    x = np.array([1, 3.5])
    p = predicao(x, thetasTeste)
    assert abs(1.1252745 - p) < 0.0001
