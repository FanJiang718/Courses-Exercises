import numpy as np

def mapFeatures(X, degree=6):
    '''
    Generate a new feature matrix consisting of all polynomial combinations of 
    the features with degree less than or equal to the specified degree. 
    '''

    # TODO
    n = X.shape[0]
    total = int(1 +(2+degree+1)*degree/2)
    F = np.zeros((n,total))
    F[:,0] = 1
    index = 1
    for i in range(1,degree+1):
        for j in range(i+1):
            F[:,index] = X[:,0]**j * X[:,1]**(i-j)
            index +=1
    return F 
