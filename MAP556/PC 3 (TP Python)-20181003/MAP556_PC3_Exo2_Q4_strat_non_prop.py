# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 2 Question 4")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

print("Estimation avec stratification non proportionnelle \n")

Esp_gY = np.sinh(1.0)
Var_gY = (1. - np.exp(-2.)) / 2

N = 1000 # Taille echantillon

# Stratification non proportionnelle

def stratificationNonProportionnelle(r):
    N1 = int(N*r)
    N2 = int(N - N1)
    
    ################
    # Completer avec N1 et N2 tirages
    # des lois conditionnelles sur les strates
    X1 = np.exp(np.random.rand(N1)*2-1)
    X2 = np.exp(np.random.rand(N2)*2-1)
    ################
    
    ################
    # Estimateur stratifie
    J_N = (np.mean(X1)+np.mean(X2))*0.5
    
    ############################################################
    # On evalue par simulation la variance de l'estimateur J_N
    var = 0.25*np.var(X1)+0.25*np.var(X2)
        
    demiLargeurIC = 1.96*np.sqrt(var/N)
    
    erreurRelative = demiLargeurIC / J_N
    
    print("Estimateur par stratification non proportionnelle, r = %1.2f \n" %r)
    
    print("Esp_gY = %1.3f Var_gY = %1.3f" %(Esp_gY, Var_gY))
    print("J_N = %1.3f  var*N = %1.3f" %(J_N, var))
    print("IC = [%1.3f,%1.3f] \n" %(J_N - demiLargeurIC, J_N + demiLargeurIC))
    
    print("erreurRelative = %1.3f" %erreurRelative)
    print("gain en nombre de simulations par rapport a MC : %1.2f" %(Var_gY/var))
    
    ############################################
    ## Trajectoires de l'estimateur stratifie pour n=1,..,N
    ############################################
    M = 10
    
    #####################
    # Completer avec M x N1 et M x N2 tirages
    # des lois conditionnelles sur les strates
    X1 = np.exp(np.random.rand(M,N1)*2-1)
    X2 = np.exp(np.random.rand(M,N2)*2-1)
    
    Y1 = np.exp(X1); Y2 = np.exp(X2)
    
    J_n = np.zeros((M,N))
    
    #####################
    # Completer avec le calcul de l'estimateur
    # stratifie pour les differentes valeurs de n
    for n in np.arange(int(1/r),N):
        n1 = int(n*r)
        n2 = n-n1
        J_n[:,n] = (np.mean(X1[:,0:n1],axis =1)+np.mean(X2[:,0:n2],axis =1))*0.5
        
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