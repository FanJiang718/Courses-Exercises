from numpy import *
import numpy.linalg as lg
#data : the data matrix
#k the number of component to return
#return the new data and  the variance that was maintained AND the principal components (ALL)
def pca(data,k):
	# Performs principal components analysis (PCA) on the n-by-p data matrix A (data)
	# Rows of A correspond to observations (wines), columns to variables.
	## TODO: Implement PCA

	# compute the mean
	# subtract the mean (along columns)
	# compute covariance matrix
	# compute eigenvalues and eigenvectors of covariance matrix
	# Sort eigenvalues
	# Sort eigenvectors according to eigenvalues
	# Project the data to the new space (k-D)
    
    mean_X = mean(data, axis = 1,keepdims=True)
    data = data - mean_X
    cov = dot(data.T, data)
    u, s, vh = lg.svd(cov)
    proj = data.dot(vh[:k,:].T)
    perc = sum(s[:k])/sum(s)
    return proj, perc, vh.T
  
