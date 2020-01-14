# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 2 Question 5")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

Esp_gY = np.sinh(1.0)
Var_gY = (1.0-np.exp(-2.))/2.

N = 1000 # Taille echantillon
M = 10 # Nombre de tirages de l'estimateur stratifie (pour l'affichage des trajectoires)

## Calcul explicite de sigma_1, sigma_2
sigma_1 = np.sqrt(0.5*(1.-np.exp(-2)) - (1.-np.exp(-1))**2)
sigma_2 = np.sqrt(0.5*(np.exp(2)-1.) - (np.exp(1)-1.)**2)

############################################
## Calculer le N1 optimal
r = sigma_1/(sigma_1 + sigma_2)

N1 = int(N *r)
N2 = int(N - N1)

############################################
## Simulation de l'estimateur par stratification
## non proportionnelle avec N1 optimal
## (meme code que la Question 4)
X1 = np.exp(np.random.rand(N1)*2-1)
X2 = np.exp(np.random.rand(N2)*2-1)

############################################
# Estimateur stratifie
J_N = (np.mean(X1)+np.mean(X2))*0.5

############################################
## Calculer la variance de l'estimateur J_N optimal.
## On peut utiliser l'expression explicite de la variance de J_N
var = (0.5*sigma_1+0.5*sigma_2)**2/N

demiLargeurIC = 1.96 * np.sqrt(var / N)
erreurRelative = demiLargeurIC / J_N

############################################
print("Estimateur par stratification non proportionnelle optimale, r_optimal = %1.3f" %r)

print("Esp_gY = %1.3f Var_gY = %1.3f" %(Esp_gY,Var_gY))
print("J_mean = %1.3f  variance_theorique = %1.3f" %(J_N, var))
print("IC = [%1.3f,%1.3f] \n" %(J_N - demiLargeurIC, J_N + demiLargeurIC))

print("erreurRelative = %1.3f" %erreurRelative)
print("gain en nombre de simulations par rapport a MC : %1.2f" %(Var_gY/var))


############################################
# Completer avec le calcul des trajectoires de 
# l'estimateur pour les differentes valeurs de n
J_n = np.zeros((M,N))

X1 = np.exp(np.random.rand(M,N1)*2-1)
X2 = np.exp(np.random.rand(M,N2)*2-1)
for n in np.arange(int(1/r),N):
    n1 = int(n*r)
    n2 = n-n1
    J_n[:,n] = (np.mean(X1[:,0:n1],axis =1)+np.mean(X2[:,0:n2],axis =1))*0.5
    
############################################
# Affichage des trajectoires 
integers1toN = np.arange(1,N+1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(integers1toN, J_n[1:10,:].T, color="b")

ax.set_ylim(1.0, 1.3)
ax.axhline(Esp_gY, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()