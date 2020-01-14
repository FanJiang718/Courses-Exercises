from numpy import *
import matplotlib.pyplot as plt
import scipy.optimize as op
from predict import predict
from mapFeatures import mapFeatures
from computeCostreg import computeCostreg
from computeGradreg import computeGradreg
from plotBoundary import plotBoundary
from sklearn.svm import SVC
import numpy as np


def stochastic_gd(X,y,l,initial_theta,learning_rate, epochs, batch_size):
    theta = initial_theta
    N_theta = len(theta)
    theta = theta.reshape(N_theta)
    N = len(y)
    #print(N)
    n_batch = N // batch_size
    loss = []
    for i in range(epochs):
        #print("----------- epoch "+str(i) + " -------------")
        index = random.permutation(N)
        X = X[index]
        y = y[index]
        for j in range(n_batch):
            #print("batch" + str(j))
            theta -= learning_rate * computeGradreg(theta, X[batch_size*j:batch_size*(j+1),:]
            ,y[batch_size*j:batch_size*j+batch_size], l)
        if N%batch_size:
            theta -= learning_rate * computeGradreg(theta, X[batch_size*n_batch:N,:],
                                                    y[batch_size*n_batch:N], l)
        loss.append(computeCostreg(theta,X,y, l))
    return theta, loss

# # Load the dataset
# Uncomment the following command if you want to load the microchip dataset
#data = loadtxt('data/microchips.csv', delimiter=',')
data = loadtxt('data/bus_train.csv', delimiter=',')
data_test = loadtxt('data/bus_test.csv', delimiter=',')
# Uncomment the following command in order to load bus dataset
#data = genfromtxt('bus.csv',delimiter=',')


# The first two columns contains the exam scores and the third column contains the label.
X = data[:, 0:2] 
y = data[:, 2]
X_test = data_test[:, 0:2] 
y_test = data_test[:, 2]

# # Plot data 
plt.plot(X[:,0][y == 1], X[:,1][y == 1], 'ro', label="c1")
plt.plot(X[:,0][y == 0], X[:,1][y == 0], 'b+', label="c2")
plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.legend(['y = 1', 'y = 0'],numpoints=1)
plt.show()

# Generate features
degree = 6
F = mapFeatures(X, degree)
F_test = mapFeatures(X_test, degree)
#print(F.shape)
# Initialize unknown parameters
w_init = zeros((F.shape[1],1))

# Regularization factor
l = 0.5

# Run minimize() to obtain the optimal coefs
#w = op.fmin_bfgs(computeCostreg,w_init,args=(F, y, l),fprime=computeGradreg)

Result = op.minimize(fun = computeCostreg, x0 = w_init, args = (F, y,l),jac = computeGradreg);
w = Result.x;


# Plot the decision boundary
plotBoundary(X, y, degree, w)
print(w)
# Compute accuracy on the training set
p = predict(array(w), F)
counter = 0
for i in range(y.size):
    if p[i] == y[i]:
        counter += 1
print('Train Accuracy: %f' % (counter / float(y.size) * 100.0))

p = predict(array(w), F_test)
counter = 0
for i in range(y_test.size):
    if p[i] == y_test[i]:
        counter += 1
print('Test Accuracy: %f' % (counter / float(y_test.size) * 100.0))



n_epoch = 100
theta_sgd, loss_sgd = stochastic_gd(F,y,l, w_init,0.0001,n_epoch,20)
print(theta_sgd)
p_sgd = predict(theta_sgd, F)
accuracy_sgd = mean(p_sgd == y)
print("Train Accuracy of SGD: %4.3f" % accuracy_sgd)
p_sgd = predict(theta_sgd, F_test)
accuracy_sgd = mean(p_sgd == y_test)
print("Test Accuracy of SGD: %4.3f" % accuracy_sgd)

plt.plot(arange(n_epoch), loss_sgd,'*')
plt.show()