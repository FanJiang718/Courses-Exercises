from numpy import *
from euclideanDistance import euclideanDistance
from simpleInitialization import simpleInitialization



def kmeans(X, k):
    # Intialize centroids
    centroids = simpleInitialization(X, k)
    
    # Initialize variables
    iterations = 0
    oldCentroids = None
    labels = zeros(X.shape[0])
    
    # ====================== ADD YOUR CODE HERE ======================
    # Instructions: Run the main k-means algorithm. Follow the steps 
    #               given in the description. Compute the distance 
    #               between each instance and each centroid. Assign 
    #               the instance to the cluster described by the closest
    #               centroid. Repeat the above steps until the centroids
    #               stop moving or reached a certain number of iterations
    #               (e.g., 100).

    for i in range(100):
        for j in range(len(X)):
            mindist = inf
            for l in range(k):
                dist = euclideanDistance(X[j,:],centroids[l])
                if dist < mindist:
                    mindist = dist
                    labels[j] = l
                    
        oldCentroids = centroids.copy()
        for l in range(k):
            centroids[l,:] = mean(X[labels==l,:], axis = 0)
        
    
    # ===============================================================
        
    return labels
