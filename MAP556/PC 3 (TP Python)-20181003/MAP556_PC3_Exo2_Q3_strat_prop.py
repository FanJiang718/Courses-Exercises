# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 2 Question 3")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

Esp_gY = np.sinh(1.0)
Var_gY = (1.0 - np.exp(-2.))/2.

N = 1000 # Taille totale de l'echantillon

# Stratification proportionnelle
N1 = int(N/2); N2 = N1

############################################
# Completer avec N1 et N2 tirages des lois
# conditionnelles sur les strates
X1 = np.exp(np.random.rand(N1)*2-1)
X2 = np.exp(np.random.rand(N2)*2-1)
############################################

############################################
# Completer avec le calcul de l'estimateur stratifie
J_N = np.mean(X1)*0.5+np.mean(X2)*0.5

############################################
# Evaluer par simulation la variance asymptotique
# dans le TCL pour l'estimateur J_N
############################################
var = np.var(X1)*0.25+np.var(X2)*0.25

demiLargeurIC = 1.96*np.sqrt(var / N)
erreurRelative = demiLargeurIC / J_N

#######
print("Estimateur par stratification proportionnelle \n")

print("Esp_gY = %1.3f Var_gY = %1.3f" %(Esp_gY, Var_gY))
print("J_N = %1.3f  variance estimee  = %1.3f" %(J_N, var))
print("IC = [%1.3f,%1.3f] \n" %(J_N - demiLargeurIC, J_N + demiLargeurIC))
print("erreurRelative = %1.3f" %erreurRelative)

print("gain en nombre de simulations par rapport a MC : %1.2f" %(Var_gY/var))

############################################
## Trajectoires de l'estimateur stratifie J_n
## pour n = 2,4,...,N
############################################
M = int(10)

############################################
# Completer avec M x N1 et M x N2 tirages
# des lois conditionnelles sur les strates
X1 = np.exp(np.random.rand(M,N1)*2-1)
X2 = np.exp(np.random.rand(M,N2)*2-1)
############################################

J_n = np.zeros((M,int(N/2)))

############################################
# Completer avec le calcul de l'estimateur
# stratifie pour n = 2,4,...,N

for n in np.arange(2, N+2, 2):
    n1 = int(n/2)
    J_n[:, n1-1] = (np.mean(X1[:,0:n1],axis =1)+np.mean(X2[:,0:n1],axis =1))*0.5
 
############################################
# Affichage des trajectoires de l'estimateur
## stratifie pour n = 2,4,...,N

evenIntegers1toN = np.arange(2,N+2,2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(evenIntegers1toN, J_n[1:10,:].T, color="b")

ax.set_ylim(1.0, 1.3)
ax.axhline(Esp_gY, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()
