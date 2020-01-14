# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.maximum(x-2.,0.)

def g_importance(z,theta=2):
    return g(z) * np.exp(-theta*z + theta*theta/2.)

# moyenne theorique des deux estimateurs
Esp_gY = 0.00849 

print("Esp_gY = %1.5f \n" %Esp_gY)

M = 1000 # Nombre de tirages
N = 1000 # Taille echantillon

integers1toN = np.arange(1,N+1) # Un vecteur contenant les entiers de 1 a N

Y = np.random.randn(M,N)

GY = g(Y) # echantillon a partir de N(0,1)

GY_importance = g_importance(Y+2.) # echantillon a partir de N(2,1)

def erreurMC(N1):
    return (np.mean(GY[:,0:N1],axis=1) - Esp_gY) * np.sqrt(N1)

def erreurImportance(N1):
    return (np.mean(GY_importance[:,0:N1],axis=1) - Esp_gY) * np.sqrt(N1)

# Affichage histogramme de l'erreur pour l'estimateur MC
# et pour l'estimateur d'importance
plt.hist(erreurMC(N), normed="True", bins=int(np.sqrt(M)), label="erreur MC")
plt.hist(erreurImportance(N), normed="True", bins=int(np.sqrt(M)), label="erreur Imp")
plt.legend(loc="best")
plt.show()