# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 3 Question 3")
print("-" * 40)

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

############################################
# Completer avec les M x N tirages
# a partir de la loi N(0,1)
# et a partir de la loi N(2,1)
Y = np.random.randn(M, N)
Y_theta = Y+theta
GY = np.mean((Y-2)*((Y-2)>0) ,axis = 1)

GY_importance = np.mean((Y_theta-2)*((Y_theta-2)>0)*np.exp(-theta*Y_theta+theta*theta*0.5) ,axis = 1)

############################################
# Completer avec le calcul des erreurs des deux estimateurs
# Output: echantillon de taille M

erreurMC = GY- Esp_gY
erreurImportance = GY_importance - Esp_gY

# Affichage de l'histogramme de l'erreur pour l'estimateur MC
# et pour l'estimateur d'importance
plt.hist(erreurMC , normed="True", bins=int(np.sqrt(M)), label="erreur MC")

plt.hist(erreurImportance, normed="True", bins=int(np.sqrt(M)), label="erreur Imp")

plt.legend(loc="best")
plt.show()