# Feature selection with the Chi^2 measure

import numpy as np
def chiSQ(x, y):
    '''
        x: features (data)
        y: output (classes)
    '''
    cl = np.unique(y) # unique number of classes
    rows = x.shape[0]
    dim = x.shape[1]
    chisq = np.zeros(dim) # initialize array (vector) for the chi^2 values
    
    # ====================== YOUR CODE HERE ======================
    # Instructions: calculate the importance for ecah feature
    for i in range(dim):
        cl_x, counts = np.unique(x[:,i], return_counts=True)
        for xx in cl_x:
            for yy in cl:
                indic_x = (x[:,i] == xx)
                indic_y = (y == yy)
                O = np.sum(indic_y[indic_x])
                E = 1./rows*np.sum(indic_x)*np.sum(indic_y)
                chisq[i] += (O-E)**2/E
    
    return chisq
