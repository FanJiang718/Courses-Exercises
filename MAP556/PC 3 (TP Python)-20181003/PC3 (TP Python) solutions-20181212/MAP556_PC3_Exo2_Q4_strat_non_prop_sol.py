# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 2 Question 4")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

print("Estimation avec stratification non proportionnelle \n")

Esp_gY = np.sinh(1.0)
Var_gY = (1.0-np.exp(-2.))/2.

N = 1000 # Taille echantillon

# Stratification non proportionnelle

def stratificationNonProportionnelle(r):
    N1 = int(N*r)
    N2 = N - N1
    
    ################
    # Completer avec N1 et N2 tirages
    # des lois conditionnelles sur les strates
    X1 = np.random.rand(N1) - 1.
    X2 = np.random.rand(N2)
    ################
    
    ################
    # Estimateur stratifie
    Y1 = np.exp(X1)
    Y2 = np.exp(X2)
    J_N = 0.5*(np.mean(Y1) + np.mean(Y2))
    
    ############################################################
    # On evalue par simulation la variance de l'estimateur J_N
    var = 0.5**2 * (np.var(Y1) / r + np.var(Y2) / (1-r) )
    
    demiLargeurIC = 1.96*np.sqrt(var)
    
    erreurRelative = demiLargeurIC / J_N
    
    print("Estimateur par stratification non proportionnelle, r = %1.2f \n" %r)
    
    print("Esp_gY = %1.4f Var_gY = %1.4f" %(Esp_gY, Var_gY))
    print("J_N = %1.4f  var*N = %1.4f" %(J_N, var))
    print("IC = [%1.4f,%1.4f] \n" %(J_N - demiLargeurIC, J_N + demiLargeurIC))
    
    print("erreurRelative = %1.4f" %erreurRelative)
    print("gain en nombre de simulations par rapport a MC : %1.4f" %(Var_gY/var))
    
    ############################################
    ## Trajectoires de l'estimateur stratifie pour n=1,..,N
    ############################################
    M = 10
    
    X1 = np.random.rand(M,N1) - 1
    X2 = np.random.rand(M,N2)
    
    Y1 = np.exp(X1); Y2 = np.exp(X2)
    
    J_n = np.zeros((M,N))
    
    for n in np.arange(int(1/r),N):
        n1 = int(n*r)
        n2 = n-n1
        J_n[:,n] = 0.5*(np.mean(Y1[:,0:n1], axis=1) + np.mean(Y2[:,0:n2], axis=1))
        
    ############################################
    # Affichage des trajectoire
    integers1toN = np.arange(1,N+1)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(integers1toN, J_n[1:10,:].T, color="b")
    
    ax.set_ylim(1.0, 1.3)
    ax.axhline(Esp_gY, color="r", label="Esperance")
    ax.legend(loc="best")
    plt.show()

stratificationNonProportionnelle(0.8)
stratificationNonProportionnelle(0.4)
stratificationNonProportionnelle(0.2)