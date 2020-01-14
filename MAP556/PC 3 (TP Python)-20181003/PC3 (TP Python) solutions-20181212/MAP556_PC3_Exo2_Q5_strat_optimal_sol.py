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
sigma_1 = np.sqrt(0.5*(1.-np.exp(-2.)) - (1.-np.exp(-1.))**2)
sigma_2 = np.sqrt(0.5*(np.exp(2.)-1.) - (np.exp(1.)-1.)**2)

## N1 optimal
r = sigma_1 / (sigma_1 + sigma_2)

N1 = int(N *r)
N2 = int(N - N1)

############################################
## Simulation de l'estimateur par stratification
## non proportionnelle avec N1 optimal
## (meme code que la Question 4)
X1 = np.random.rand(M,N1) - 1.
X2 = np.random.rand(M,N2)

############################################
# Estimateur stratifie
Y1 = np.exp(X1)
Y2 = np.exp(X2)
J_N = 0.5*(np.mean(Y1,axis=1) + np.mean(Y2,axis=1))[0]

############################################
## On utilise l'expression explicite de la variance de J_N
variance_theorique = ((sigma_1 + sigma_2)/2)**2

demiLargeurIC = 1.96 * np.sqrt(variance_theorique / N)
erreurRelative = demiLargeurIC / J_N

############################################
print("Estimateur par stratification non proportionnelle optimale, r_optimal = %1.3f" %r)

print("Esp_gY = %1.3f Var_gY = %1.3f" %(Esp_gY,Var_gY))
print("J_mean = %1.3f  variance_theorique = %1.3f" %(J_N, variance_theorique))
print("IC = [%1.3f,%1.3f] \n" %(J_N - demiLargeurIC, J_N + demiLargeurIC))

print("erreurRelative = %1.3f" %erreurRelative)
print("gain en nombre de simulations par rapport a MC : %1.2f" %(Var_gY/variance_theorique))

############################################
# Trajectoires de l'estimateur stratifie 
# pour n=1,..,N
J_n = np.zeros((M,N))

for n in np.arange(int(1/r),N):
    n1 = int(n*r)
    n2 = n-n1
    J_n[:,n] = 0.5*(np.mean(Y1[:,0:n1], axis=1) + np.mean(Y2[:,0:n2], axis=1))
    
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
