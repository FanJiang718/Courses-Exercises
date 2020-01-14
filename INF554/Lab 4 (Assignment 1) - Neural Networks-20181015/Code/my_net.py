import numpy as np
import tensorflow as tf
from sklearn.utils import shuffle
from time import clock

###############################################################
#
# Important notes: 
# - Do not change any of the existing functions or parameter names, 
#       except in __init__, you may add/change parameter names/defaults values.
# - In __init__ set default values to the best ones, e.g., learning_rate=0.1
# - Training epochs/iterations should not be a parameter to __init__,
#   To train/test your network, we will call fit(...) until time (2 mins) runs out.
#
###############################################################

class Network():
    def __init__(self, learning_rate=0.005):
        ''' initialize the classifier with default (best) parameters '''

        self.alpha = learning_rate
        self.batch_size = 100
        self.display_step = 10
        
        self.d_X = 294
        self.d_Y = 6
        self.x = tf.placeholder(tf.float32,[None, self.d_X],name = 'x')
        self.y = tf.placeholder(tf.float32,[None, self.d_Y], name = 'y')
        
        
        self.d_h1 = 64
        self.d_h2 = 32
        self.d_h3 = 16
        W = {"h1": tf.Variable(tf.random_normal([self.d_X, self.d_h1])),
             "h2": tf.Variable(tf.random_normal([self.d_h1, self.d_h2])),
             "h3": tf.Variable(tf.random_normal([self.d_h2, self.d_h3])),
             "out": tf.Variable(tf.random_normal([self.d_h3, self.d_Y]))}
        
        b = {"h1": tf.Variable(tf.random_normal([self.d_h1])),
             "h2": tf.Variable(tf.random_normal([self.d_h2])),
             "h3": tf.Variable(tf.random_normal([self.d_h3])),
             "out": tf.Variable(tf.random_normal([self.d_Y]))}
        
        self.layer1 = tf.nn.sigmoid(tf.matmul(self.x,W["h1"])+b["h1"])
        self.layer2 = tf.nn.sigmoid(tf.matmul(self.layer1,W["h2"])+b["h2"])
        self.layer3 = tf.nn.sigmoid(tf.matmul(self.layer2,W["h3"])+b["h3"])
        self.pred_logits = tf.matmul(self.layer3,W["out"])+b["out"]
        self.pred = tf.nn.sigmoid(self.pred_logits)
        
        
        """
        self.d_h1 = 128
        self.d_h2 = 64
        self.d_h3 = 32
        self.d_h4 = 16
        W = {"h1": tf.Variable(tf.random_normal([self.d_X, self.d_h1])),
             "h2": tf.Variable(tf.random_normal([self.d_h1, self.d_h2])),
             "h3": tf.Variable(tf.random_normal([self.d_h2, self.d_h3])),
             "h4": tf.Variable(tf.random_normal([self.d_h3, self.d_h4])),
             "out": tf.Variable(tf.random_normal([self.d_h4, self.d_Y]))}
        
        b = {"h1": tf.Variable(tf.random_normal([self.d_h1])),
             "h2": tf.Variable(tf.random_normal([self.d_h2])),
             "h3": tf.Variable(tf.random_normal([self.d_h3])),
             "h4": tf.Variable(tf.random_normal([self.d_h4])),
             "out": tf.Variable(tf.random_normal([self.d_Y]))}
        
        self.layer1 = tf.nn.sigmoid(tf.matmul(self.x,W["h1"])+b["h1"])
        self.layer2 = tf.nn.sigmoid(tf.matmul(self.layer1,W["h2"])+b["h2"])
        self.layer3 = tf.nn.sigmoid(tf.matmul(self.layer2,W["h3"])+b["h3"])
        self.layer4 = tf.nn.sigmoid(tf.matmul(self.layer3,W["h4"])+b["h4"])
        self.pred_logits = tf.matmul(self.layer4,W["out"])+b["out"]
        self.pred = tf.nn.sigmoid(self.pred_logits)
        """
        
        #self.cost = -tf.reduce_sum(self.y*tf.log(self.pred)+(1-self.y)*tf.log(1-self.pred))
        self.cost = tf.reduce_sum(tf.nn.sigmoid_cross_entropy_with_logits(labels = self.y, logits = self.pred_logits))
        self.optimizer = tf.train.AdamOptimizer(self.alpha).minimize(self.cost)
        
        self.init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(self.init)
            

    def fit(self,X,Y,warm_start=True,n_epochs=10):
        ''' train the network, and if warm_start, then do not reinit. the network
            (if it has already been initialized)
        '''
        X = np.float32(X)
        Y = np.float32(Y)
        self.n_labels = Y.shape[1]
        self.n = Y.shape[0]
        total_batch = self.n//self.batch_size
        if not warm_start:
            self.sess.run(self.init)
         
        
        for epoch in range(n_epochs):
            X,Y = shuffle(X,Y)
            avg_cost = 0
            for i in range(total_batch-1):
                x_batch, y_batch = X[i*self.batch_size:(i+1)*self.batch_size,:], Y[i*self.batch_size:(i+1)*self.batch_size,:]
                _, c = self.sess.run([self.optimizer, self.cost], 
                                feed_dict={'x:0': x_batch, 'y:0':y_batch })
                avg_cost += c / total_batch
                
            _, c = self.sess.run([self.optimizer, self.cost], 
                                feed_dict={'x:0': X[(total_batch-1)*self.batch_size:],
                                'y:0': Y[(total_batch-1)*self.batch_size:]})
            avg_cost += c / total_batch
            if (epoch+1) % self.display_step == 0:
                print("Epoch: "+str(epoch+1)+", cost={}".format(avg_cost))

        #print("Optimization Finished!")
        
        return self

    def predict_proba(self,X):
        ''' return a matrix P where P[i,j] = P(Y[i,j]=1), 
        for all instances i, and labels j. '''

        X = np.float32(X)
        return self.pred.eval(session = self.sess, feed_dict={'x:0': X})

    def predict(self,X):
        ''' return a matrix of predictions for X '''
        return (self.predict_proba(X) >= 0.5).astype(int)

