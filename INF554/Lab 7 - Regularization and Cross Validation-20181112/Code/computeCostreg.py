from numpy import *
from sigmoid import sigmoid

def computeCostreg(theta, X, y, l):
    # Computes the cost of using theta as the parameter for regularized logistic regression.
    
    m = X.shape[0] # number of training examples
    J = 0.

    # ====================== YOUR CODE HERE ======================
    # Instructions: Calculate the error J of the decision boundary
    #               that is described by theta  (see the assignment 
    #				for more details).
    
    
    J = -1./m* sum(y*log(sigmoid(dot(X,theta)) + 1e-11)+(1-y)*log(1-sigmoid(dot(X,theta))+1e-11))
    J = J + 0.5*l/m* sum(theta[1:]*theta[1:])

    # =============================================================
    
    return J



