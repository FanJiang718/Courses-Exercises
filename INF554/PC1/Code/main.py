from numpy import *
from matplotlib.pyplot import *
from scipy.linalg import inv
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPRegressor
from tools import MSE

# Load the data

data = loadtxt('data/data_train.csv', delimiter=',')

# Prepare the data

X = data[:,0:-1]
y = data[:,-1]

# Inspect the data

#figure()
#hist(X[:,1], 10)

# <TASK 1>

figure(figsize = (15,5))
subplot(1,2,1)
hist(X[:,1])
title('X2')
subplot(1,2,2)
hist(X[:,2])
title('X3')
show()

figure()
plot(X[:,1],X[:,2], 'o')
xlabel('x2')
ylabel('x3')

figure()
plot(X[:,0], y, 'o')
xlabel('x1')
ylabel('y')
show()

# <TASK 2>

for i in range(len(y)):
    if y[i] > 7:
        y[i] = 0
        
meanX= mean(X,axis = 0)
stdX = std(X, axis = 0)
X = (X-meanX)/stdX


# Standardization

# <TASK 2>

# Feature creation

from tools import poly_exp
Z = poly_exp(X,2)

Z = column_stack([ones(len(Z)), Z])

# Building a model

# <TASK 3>

w = dot(linalg.inv(dot(Z.T, Z)), dot(Z.T,y))
print("w = " + str(w))

# Evaluation 

test = loadtxt('data/data_test.csv', delimiter=',')
X_test = test[:,0:-1]
y_test = test[:,-1]
X_test = (X_test- meanX)/stdX
Z_test = poly_exp(X_test,2)
Z_test = column_stack([ones(len(Z_test)), Z_test])
y_pred = dot(Z_test,w)

# <TASK 4>

mse_test = MSE(y_test, y_pred)
y_baseline = mean(y)
mse_baseline = MSE(y_test, y_baseline)
print('MSE on test data: ' +str(mse_test))
print('MSE baseline: ' +str(mse_baseline))



# <TASK 5>
# <TASK 6>
# <TASK 7>
MSE_train = []
MSE_test = []
xx = [i for i in range(1,8)]
for i in xx:
    Z_train = poly_exp(X,i)
    Z_train = column_stack([ones(len(Z_train)), Z_train])
    w = dot(linalg.inv(dot(Z_train.T, Z_train)), dot(Z_train.T,y))
    Z_test = poly_exp(X_test,i)
    Z_test = column_stack([ones(len(Z_test)), Z_test])
    y_pred_test = dot(Z_test,w)
    y_pred_train = dot(Z_train,w)
    MSE_test.append(MSE(y_test, y_pred_test))
    MSE_train.append((MSE(y,y_pred_train)))
    
figure()
plot(xx, MSE_train, 'b', label = 'MSE_train')
plot(xx, MSE_test, 'r', label = 'MSE_test')
legend(loc = 'best')
title("comparison between MSE_train and MSE_test")
show()

# <TASK 8: You will need to make changes from '# Feature creation'
#          To get the exact results, you will need to reverse the second part of Task 7 (your own modifications)>


MSE_train_PCA = []
MSE_test_PCA = []
xx = [i for i in range(1,8)]
pca = PCA(n_components = 2)

for i in xx:
    Z_train = poly_exp(X,i)
    Z_train = column_stack([ones(len(Z_train)), Z_train])
    Z_compresed_train = pca.fit_transform(Z_train)
    w = dot(linalg.inv(dot(Z_compresed_train.T, Z_compresed_train)), dot(Z_compresed_train.T,y))
    Z_test = poly_exp(X_test,i)
    Z_test = column_stack([ones(len(Z_test)), Z_test])
    Z_compresed_test = pca.fit_transform(Z_test)
    y_pred_test = dot(Z_compresed_test,w)
    y_pred_train = dot(Z_compresed_train,w)
    MSE_test_PCA.append(MSE(y_test, y_pred_test))
    MSE_train_PCA.append((MSE(y,y_pred_train)))
    
figure()
plot(xx, MSE_train_PCA, 'b', label = 'MSE_train')
plot(xx, MSE_test_PCA, 'r', label = 'MSE_test')
legend(loc = 'best')
title("comparison between MSE_train and MSE_test after PCA")
show()
print("So the PCA will not improve the result")


"""
use neural network to fit the data
"""

nn = MLPRegressor((30,20,10,5,3),max_iter = 2000)
nn.fit(X,y)
y_pred_test = nn.predict(X_test)
y_pred_train = nn.predict(X)
mse_test_nn = MSE(y_test, y_pred_test)
mse_train_nn = MSE(y, y_pred_train)
print("The result for the neural network")
print('MSE on test data: ' +str(mse_test_nn))
print('MSE on train data: ' +str(mse_train_nn))
print('Obviously, the neural network gives better result')
