# Feature selection with the Information Gain measure

from numpy import *
from math import log

def infogain(x, y):
    '''
        x: features (data)
        y: output (classes)
    '''
    info_gains = zeros(x.shape[1]) # features of x
    
    # calculate entropy of the data *hy* with regards to class y
    cl = unique(y)
    hy = 0
    for i in range(len(cl)):
        c = cl[i]
        py = float(sum(y==c))/len(y) # probability of the class c in the data
        hy = hy+py*log(py,2)
    
    hy = -hy

    # ====================== YOUR CODE HERE ================================
    # Instructions: calculate the information gain for each column (feature)
    dims = x.shape[1]
    for d in range(dims):
        cl_x, counts = unique(x[:,d], return_counts=True)
        info_gains[d] = hy
        for j in range(len(cl_x)):
            info_gains[d] -= counts[j]/len(y)* entropy(y[x[:,d] == cl_x[j]])
        print(info_gains[d])
    return info_gains
    
def entropy(y):
    cl = unique(y)
    hy = 0
    for i in range(len(cl)):
        c = cl[i]
        py = float(sum(y==c))/len(y) # probability of the class c in the data
        hy = hy+py*log(py,2)
    
    return -hy