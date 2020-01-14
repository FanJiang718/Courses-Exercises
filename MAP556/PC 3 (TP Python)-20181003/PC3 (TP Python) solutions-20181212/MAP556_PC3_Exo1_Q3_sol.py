# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 1 Question 3")
print ("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

N = 500 # Taille echantillon
M = 1000 # Nombre de tirages des estimateurs

integers1toN = np.arange(1,N+1) # Un vecteur contenant les entiers de 1 a N

Esp_gY = np.exp(1.)-1.
m_r = 1.5

###############
# Echantillons
X = np.random.rand(M,N) 
Y = np.exp(X)

Ycontrole = Y - (X+1) + m_r
###############

############################################
# Echantillons de taille M des deux estimateurs 

I_N = np.mean(Y, axis=1)

Ic_N = np.mean(Ycontrole, axis=1)

############################################
## Affichage des histogrammes des erreurs
## pour les deux estimateurs

plt.hist(I_N - Esp_gY, normed="True", bins=int(np.sqrt(M)), label="MC")

plt.hist(Ic_N - Esp_gY, normed="True", bins=int(np.sqrt(M)), label="Controle")

plt.title("Estimation avec variable de controle, N = %1.0f" %N)

plt.legend(loc="best")
plt.show()