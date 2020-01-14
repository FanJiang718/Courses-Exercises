from numpy import *
from numpy.linalg import norm
from queue import PriorityQueue
def kNN_prediction(k, X, labels, x):
    '''
    kNN classification of x
    -----------------------
        Input: 
        k: number of nearest neighbors
        X: training data           
        labels: class labels of training data
        x: test instance

        return the label to be associated with x

        Hint: you may use the function 'norm' 
    '''

    # TASK
    pqueue = PriorityQueue()
    for i in range(len(X)):
        dist = norm((X[i,:]-x)*(X[i,:]-x))
        pqueue.put((dist,labels[i]))
    
    label_dist = {}
    for i in range(k):
        dist, label = pqueue.get()
        label_dist[label] = label_dist.get(label,0) +1
 
    max_value = 0
    max_label = None
    for key, value in label_dist.items():
        if value > max_value:
            max_value = value
            max_label = key
    return max_label

 
