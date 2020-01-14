import numpy as np

def gaussianKernel(X1, X2, sigma = 0.1):
    m = X1.shape[0]
    K = np.zeros((m,X2.shape[0]))
    
    # ====================== YOUR CODE HERE =======================
    # Instructions: Calculate the Gaussian kernel (see the assignment
    #				for more details).
    if m >1:
        X1_square = np.sum(X1*X1,axis = 1,keepdims = True)
        X2_square = (np.sum(X2*X2,axis =1)).reshape((-1,m))
        print(X1_square.shape)
        print(X2_square.shape)
        K = np.exp(-(X1_square-2*np.dot(X1,X2.T)+X2_square)/(2*sigma*sigma))
    else:
        K = np.exp(-np.sum((X1 - X2)*(X1-X2),axis =1)/(2*sigma*sigma))
        K = K.reshape(1,-1)
    # =============================================================

    return K
