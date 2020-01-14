from numpy import *
from euclideanDistance import euclideanDistance

def findClosestNeighbours(data, N):
    
    closestNeighbours = zeros((data.shape[0], N))
    distances = zeros(data.shape[0])

    # ====================== ADD YOUR CODE HERE ======================
    # Instructions: Find the N closest instances of each instance
    #               using the euclidean distance.
    
    for i in range(len(data)):
        for j in range(len(data)):
            distances[j] = euclideanDistance(data[i,:], data[j,:])
        distances[i] = inf
        tmp = argpartition(distances, N)
        closestNeighbours[i,:] = tmp[:N]
        #print(closestNeighbours[i,:])
    
    
    # =============================================================
    
    return closestNeighbours.astype(int)
