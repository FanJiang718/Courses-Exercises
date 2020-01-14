# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 2 Questions 2")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

print("Estimation avec variable antithetique \n")

N = 1000 # Taille echantillon

integers1toN = np.arange(1,N+1) # Un vecteur contenant les entiers de 1 a N

Esp_gY = np.sinh(1.0);
Var_gY = (1.0-np.exp(-2.))/2.

############################################
# Completer avec N de tirages de la loi uniforme [-1,1]
# et les tirages antithetiques
X = 2.0*np.random.rand(N) - 1.0
Z = 0.5*(np.exp(X) + np.exp(-X))
#
############################################

############################################
# Completer avec le calcul de l'estimateur antithetique
mean = np.mean(Z)
var = np.var(Z)
demiLargeurIC = 1.96 * np.sqrt(var / N)
############################################

print("Estimateur antithetique \n")

print("Esp_gY = %1.3f" %(Esp_gY))
print("I_prime_mean = %1.3f  var empirique = %1.3f" %(mean, var))
print("Intervalle de confiance 95%% pour E[g(Y)] = [ %1.3f , %1.3f ] \n" %(mean - demiLargeurIC, mean + demiLargeurIC))
print("erreur relative = %1.3f" %(demiLargeurIC/mean))
print("gain en nombre de simulations par rapport a MC : %1.2f" %(Var_gY/var))

############################################
## Trajectoires de la moyenne empirique
############################################
M = 10

############################################
# Evaluer M trajectoires de l'estimateur empirique I'_n
M = 10
X = 2.0*np.random.rand(M,N) - 1.0
Z = 0.5*(np.exp(X) + np.exp(-X))

############################################
# Completer avec le calcul des trajectoires
# de l'estimateur antithetique
I_prime_n = np.cumsum(Z, axis=1)/integers1toN
############################################

# Affichage des trajectoires de l'estimateur
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(integers1toN, I_prime_n.T, color="b")

ax.set_xlim(0, N)
ax.set_ylim(1.0, 1.3)
ax.axhline(Esp_gY, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()