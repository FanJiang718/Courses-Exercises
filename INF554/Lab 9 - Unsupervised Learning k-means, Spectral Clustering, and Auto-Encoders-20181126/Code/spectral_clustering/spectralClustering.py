from numpy import *
from scipy.cluster.vq import kmeans2
from scipy.linalg import eigh

def spectralClustering(W, k):

    # ====================== ADD YOUR CODE HERE ======================
    # Instructions: Perform spectral clustering to partition the 
    #               data into k clusters. Implement the steps that
    #               are described in Algorithm 2 on the assignment.    
    D = diag([sum(W[i,:]) for i in range(len(W))])
    L = D-W
	
    w,v = eigh(L,eigvals= (0,k-1))
    centroids, labels = kmeans2(v, k)
    
    
    # =============================================================
    

    return labels
