import numpy as np
from my_net import Network
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

###############################################################
# This is an example script, you may modify it as you wish
###############################################################

# Load and parse the data (N instances, D features, L=3 labels)
#path = "/Users/FanJiang/Documents/Polytechnique/Cours/INF554/Lab 4 (Assignment 1) - Neural Networks-20181015/Code/"
#XY = np.genfromtxt(path + 'data/scene.csv', skip_header=1, delimiter=",")
XY = np.genfromtxt('data/scene.csv', skip_header=1, delimiter=",")
N,DL = XY.shape
L = 6
D = DL - L
Y = XY[:,0:L].astype(int)
X = XY[:,L:D+L]

# Split into train/test sets

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4,random_state = 42)
"""
n = int(N*6/10)
X_train = X[0:n]
Y_train = Y[0:n]
X_test = X[n:]
Y_test = Y[n:]
"""
from time import clock
t0 = clock()


# Test our classifier 
h = Network()

"""
t0= clock() 
h.fit(X_train,Y_train,n_epochs=epochs)
print("Trainning time: "+str(clock()-t0))
"""

time_h = []
hamming_loss = []
time_limit = 5
t0 = clock()
while clock()-t0 <= time_limit:
    h.fit(X_train,Y_train,n_epochs=10)
    time_h.append(clock()-t0)
    Y_pred = h.predict(X_test)
    hamming_loss.append(np.mean(Y_pred != Y_test))
  


Y_pred = h.predict(X_test)
print(Y_test)
print(Y_pred)
loss = np.mean(Y_pred != Y_test)
print("Hamming loss: ", loss)

print("Hamming loss for prediction of all 0: "+str(np.mean(np.zeros(Y_test.shape) != Y_test)))



from sklearn.neural_network import MLPClassifier
t0 = clock()
nn = MLPClassifier((64,32,16), max_iter = 500)
nn.fit(X_train,Y_train)
Y_pred = nn.predict(X_test)
t_nn = clock() - t0
#print(Y_test)
#print(Y_pred)
loss_nn = np.mean(Y_pred != Y_test)
print("Hamming loss for neural network of Sklearn: ", loss_nn)


from sklearn.neighbors import KNeighborsClassifier
t0 = clock()
knn = KNeighborsClassifier()
knn.fit(X_train,Y_train)
Y_pred = knn.predict(X_test)
t_knn = clock() - t0
#print(Y_test)
#print(Y_pred)
loss_knn = np.mean(Y_pred != Y_test)
print("Hamming loss for knn classifier: ", loss_knn)

from sklearn.tree import DecisionTreeClassifier
t0 = clock()
tree = DecisionTreeClassifier()
tree.fit(X_train,Y_train)
Y_pred = tree.predict(X_test)
t_tree = clock() - t0
#print(Y_test)
#print(Y_pred)
loss_tree = np.mean(Y_pred != Y_test)
print("Hamming loss for decision tree classifier: ", loss_tree)

from sklearn.multiclass import OneVsRestClassifier
t0 = clock()
onerest = OneVsRestClassifier(knn)
onerest.fit(X_train,Y_train)
Y_pred = onerest.predict(X_test)
t_onerest = clock() - t0
#print(Y_test)
#print(Y_pred)
loss_onerest = np.mean(Y_pred != Y_test)
print("Hamming loss for One vs Rest classifier: ", loss_onerest)

from sklearn.multioutput import ClassifierChain
t0 = clock()
classfierchain = ClassifierChain(knn)
classfierchain.fit(X_train,Y_train)
Y_pred = classfierchain.predict(X_test)
t_chain = clock() - t0
#print(Y_test)
#print(Y_pred)
loss_chain = np.mean(Y_pred != Y_test)
print("Hamming loss for classifier chain: ", loss_chain)


arr_epoch = np.arange(1,len(time_h)+1)*10

plt.figure(figsize = (12, 9))
plt.plot(arr_epoch, time_h, label = 'my network', c = 'k')
plt.axhline(t_nn,c= 'r', label = 'Default network of Sklearn')
plt.axhline(t_knn,c = 'g', label = 'K-nearst neighbor classifier', )
plt.axhline(t_tree, c = 'b', label = 'Decision tree classifier')
plt.axhline(t_onerest,c = 'y', label = 'OneVsRest classifier')
plt.axhline(t_chain, c = 'c', label = 'classifier chain', )
plt.xlabel("Epoches")
plt.ylabel("Time")
plt.legend(loc = 'best')
plt.title("Trainning time vs. Epoches of my network, comparing with other benchmarks")
plt.show()

plt.figure(figsize = (12, 9))
plt.plot(arr_epoch, hamming_loss, label = 'my network', c ='k')
plt.axhline(loss_nn, c = 'r', label = 'Default network of Sklearn')
plt.axhline(loss_knn, c = 'g', label = 'K-nearst neighbor classifier')
plt.axhline(loss_tree, c = 'b', label = 'Decision tree classifier')
plt.axhline(loss_onerest, c = 'y', label = 'OneVsRest classifier')
plt.axhline(loss_chain, c = 'c', label = 'classifier chain')
plt.xlabel("Epoches")
plt.ylabel("Hamming loss")
plt.legend(loc = 'best')
plt.title("Hamming loss vs. Epoches of my network, comparing with other benchmarks")
plt.show()


