from numpy import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
import numpy.linalg as lg


# Load the "gatlin" image data
X = loadtxt('gatlin.csv', delimiter=',')

#================= ADD YOUR CODE HERE ====================================
# Perform SVD decomposition
## TODO: Perform SVD on the X matrix
# Instructions: Perform SVD decomposition of matrix X. Save the 
#               three factors in variables U, S and V
#
u,s,vh = lg.svd(X)


#=========================================================================

# Plot the original image
plt.figure(1)
plt.imshow(X,cmap = cm.Greys_r)
plt.title('Original image (rank 480)')
plt.axis('off')
plt.draw()


#================= ADD YOUR CODE HERE ====================================
# Matrix reconstruction using the top k = [10, 20, 50, 100, 200] singular values
## TODO: Create four matrices X10, X20, X50, X100, X200 for each low rank approximation
## using the top k = [10, 20, 50, 100, 200] singlular values 
#

k = [10, 20, 50, 100, 200]
X5 = u[:,:5].dot(dot(diag(s[:5]), vh[:5,:]))
X20 = u[:,:20].dot(dot(diag(s[:20]), vh[:20,:]))
X50 = u[:,:50].dot(dot(diag(s[:50]), vh[:50,:]))
X100 = u[:,:100].dot(dot(diag(s[:100]), vh[:100,:]))
X200 = u[:,:200].dot(dot(diag(s[:200]), vh[:200,:]))
#=========================================================================



#================= ADD YOUR CODE HERE ====================================
# Error of approximation
## TODO: Compute and print the error of each low rank approximation of the matrix
# The Frobenius error can be computed as |X - X_k| / |X|
#
err5 = sqrt(sum((X-X5)*(X-X5)))/sqrt(sum(X*X))
err20 = sqrt(sum((X-X20)*(X-X20)))/sqrt(sum(X*X))
err50 = sqrt(sum((X-X50)*(X-X50)))/sqrt(sum(X*X))
err100 = sqrt(sum((X-X100)*(X-X100)))/sqrt(sum(X*X))
err200 = sqrt(sum((X-X200)*(X-X200)))/sqrt(sum(X*X))

print(err5)
print(err20)
print(err50)
print(err100)
print(err200)



#=========================================================================



# Plot the optimal rank-k approximation for various values of k)
# Create a figure with 6 subfigures
plt.figure(2)

# Rank 10 approximation
plt.subplot(321)
plt.imshow(X5,cmap = cm.Greys_r)
plt.title('Best rank' + str(5) + ' approximation')
plt.axis('off')

# Rank 20 approximation
plt.subplot(322)
plt.imshow(X20,cmap = cm.Greys_r)
plt.title('Best rank' + str(20) + ' approximation')
plt.axis('off')

# Rank 50 approximation
plt.subplot(323)
plt.imshow(X50,cmap = cm.Greys_r)
plt.title('Best rank' + str(50) + ' approximation')
plt.axis('off')

# Rank 100 approximation
plt.subplot(324)
plt.imshow(X100,cmap = cm.Greys_r)
plt.title('Best rank' + str(100) + ' approximation')
plt.axis('off')

# Rank 200 approximation
plt.subplot(325)
plt.imshow(X200,cmap = cm.Greys_r)
plt.title('Best rank' + str(200) + ' approximation')
plt.axis('off')

# Original
plt.subplot(326)
plt.imshow(X,cmap = cm.Greys_r)
plt.title('Original image (Rank 480)')
plt.axis('off')

plt.draw()


#================= ADD YOUR CODE HERE ====================================
# Plot the singular values of the original matrix
## TODO: Plot the singular values of X versus their rank k

nn = arange(len(s))
plt.figure()
plt.plot(nn,s)
plt.show()

#=========================================================================

plt.show() 
