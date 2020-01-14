from numpy import *
from sigmoid import sigmoid

def computeGradreg(theta, X, y, l):
    # Computes the gradient of the cost with respect to the parameters.

    m = X.shape[0] # number of training examples
    d_x = X.shape[1]
    #grad = zeros_like(theta) #initialize gradient
    grad = zeros(d_x)
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the gradient of cost for each theta,
    # as described in the assignment.
    
    
    
    N_y = len(y)
    N_theta = len(theta)
    theta = theta.reshape(N_theta)
    y = y.reshape(N_y)
    assert m == N_y
    assert d_x == N_theta
    y_pred = sigmoid(dot(X,theta))
    grad[0] = 1./m* dot(X[:,0].T,(y_pred - y))
    grad[1:] = 1./m* dot(X[:,1:].T, (y_pred - y))
    grad[1:] += l/m* theta[1:]
    #grad[0] = 1./m* sum((sigmoid(dot(X,theta)) - y.reshape((N_y,1)))*X[:,0])
    #grad[1:] = 1./m* sum((sigmoid(dot(X,theta)) - y.reshape((N_y,1)))*X[:,1:], axis = 0)
    #grad[1:] += l/m* theta[1:,0]
    #print(grad.shape)
    return grad
    
