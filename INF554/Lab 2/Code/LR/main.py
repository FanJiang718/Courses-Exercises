from numpy import *
import matplotlib.pyplot as plt
import scipy.optimize as op
from numpy.random import permutation

def sigmoid(z):
    # Computes the sigmoid of z.

    # ====================== YOUR CODE HERE ======================
    # Instructions: Implement the sigmoid function.
    
    return 1./(1. + exp(-z))
    # =============================================================
             

def cost(theta, X, y): 
    # Computes the cost using theta as the parameters for logistic regression. 
    
    # ====================== YOUR CODE HERE ======================
    # Instructions: Calculate the error J of the decision boundary
    #               that is described by theta (see the assignment 
    #               for more details).
    N = len(y)
    J = -1./N* sum(y*log(sigmoid(dot(X,theta)) + 1e-10)+(1-y)*log(1-sigmoid(dot(X,theta))+1e-10))
    
    return J
    # =============================================================
    


def compute_grad(theta, X, y):
    # Computes the gradient of the cost with respect to
    # the parameters.
    
    grad = zeros(size(theta)) # initialize gradient
    
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the gradient of cost for each theta.
    N_x, d_x = X.shape
    N_y = len(y)
    N_theta = len(theta)
    theta = theta.reshape((N_theta,1))
    assert N_x == N_y
    # =============================================================
    grad = 1./N_y* sum((sigmoid(dot(X,theta)) - y.reshape((N_y,1)))*X, axis = 0)
    return grad.reshape((size(theta),1))




def predict(theta, X):
    # Predict whether each label is 0 or 1 using learned logistic 
    # regression parameters theta. The threshold is set at 0.5
    
    # ====================== YOUR CODE HERE ======================
    # Instructions: Predict the label of each instance of the
    #               training set.
    
    probs = sigmoid(dot(X,theta))
    
    return probs > 0.5
    # =============================================================

def stochastic_gd(X,y,initial_theta,learning_rate, epochs, batch_size):
    theta = initial_theta
    N_theta = len(theta)
    N = len(y)
    #print(N)
    n_batch = N // batch_size
    loss = []
    for i in range(epochs):
        #print("----------- epoch "+str(i) + " -------------")
        index = permutation(N)
        X = X[index]
        y = y[index]
        for j in range(n_batch):
            #print("batch" + str(j))
            theta -= learning_rate * compute_grad(theta, X[batch_size*j:batch_size*(j+1)]
            ,y[batch_size*j:batch_size*j+batch_size])
        if N%batch_size:
            theta -= learning_rate * compute_grad(theta, X[batch_size*n_batch:N],
                                                    y[batch_size*n_batch:N])
        loss.append(cost(theta,X,y))
    return theta, loss

#======================================================================
# Load the dataset
# The first two columns contains the exam scores and the third column
# contains the label.
data = loadtxt('./data/data.txt', delimiter=',')
 
X = data[:, 0:2]
y = data[:, 2]

# Plot data 
pos = where(y == 1) # instances of class 1
neg = where(y == 0) # instances of class 0
plt.scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
plt.scatter(X[neg, 0], X[neg, 1], marker='x', c='r')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend(['Admitted', 'Not Admitted'])
plt.show()


#Add intercept term to X
X_new = ones((X.shape[0], 3))
X_new[:, 1:3] = X
X = X_new

# Initialize fitting parameters
initial_theta = random.randn(3,1)*0.1





# Run minimize() to obtain the optimal theta
Result = op.minimize(fun = cost, x0 = initial_theta, args = (X, y), method = 'TNC',jac = compute_grad);
theta = Result.x;

# Plot the decision boundary
plot_x = array([min(X[:, 1]) - 2, max(X[:, 2]) + 2])
plot_y = (- 1.0 / theta[2]) * (theta[1] * plot_x + theta[0])
plt.plot(plot_x, plot_y)
plt.scatter(X[pos, 1], X[pos, 2], marker='o', c='b')
plt.scatter(X[neg, 1], X[neg, 2], marker='x', c='r')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend(['Decision Boundary', 'Admitted', 'Not Admitted'])
plt.show()

# Compute accuracy on the training set
p = predict(array(theta), X)
# Evaluation
accuracy = mean(p == y)
print("\nAccuracy: %4.3f" % accuracy)
loss = cost(theta, X, y)
print("loss: "+ str(loss))



n_epoch = 100
theta_sgd, loss_sgd = stochastic_gd(X,array(y),initial_theta,0.0001,n_epoch,15)
print(theta_sgd)
p_sgd = predict(array(theta_sgd), X)
accuracy_sgd = mean(p_sgd == y)
print("\nAccuracy of SGD: %4.3f" % accuracy_sgd)

plot_x = array([min(X[:, 1]) - 2, max(X[:, 2]) + 2])
plot_y = (- 1.0 / theta_sgd[2]) * (theta_sgd[1] * plot_x + theta_sgd[0])
plt.plot(plot_x, plot_y)
plt.scatter(X[pos, 1], X[pos, 2], marker='o', c='b')
plt.scatter(X[neg, 1], X[neg, 2], marker='x', c='r')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend(['Decision Boundary', 'Admitted', 'Not Admitted'])
plt.show()






plt.plot(arange(n_epoch), loss_sgd,'*')
plt.show()
