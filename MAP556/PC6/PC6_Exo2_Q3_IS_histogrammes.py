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


############################################
# Completer avec M x N tirages des 
# echantillons a partir de la loi N(0,1)
# et a partir de la loi N(2,1)
GY = ?????

GY_importance = ?????

############################################
# Completer avec le calcul des erreurs des deux estimateurs
# Echantillon de taille M

erreurMC = ?????
erreurImportance = ?????

# Affichage de l'histogramme de l'erreur pour l'estimateur MC
# et pour l'estimateur d'importance
plt.hist(erreurMC , normed="True", bins=int(np.sqrt(M)), label="erreur MC")

plt.hist(erreurImportance, normed="True", bins=int(np.sqrt(M)), label="erreur Imp")

plt.legend(loc="best")
plt.show()