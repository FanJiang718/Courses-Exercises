# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 2 Question 1")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt

N = 1000 # Taille echantillon

integers1toN = np.arange(1,N+1) # Un vecteur contenant les entiers de 1 a N

Esp_gY = np.sinh(1.0)
Var_gY = (1.0-np.exp(-2.))/2.

############################################
# Completer avec N tirages de la loi uniforme [-1,1]
# et les tirages de Y = exp(X)
X = 2.0*np.random.rand(N)-1.0
Y = np.exp(X)
############################################

############################################
# Stocker dans 'mean' l'estimation MC de E[g(Y)]
# dans 'var' la variance empirique et dans 'demiLargeurIC'
# la demi-largeur de l'intervalle de confiance 
# asymptotique a 95% pour E[g(Y)]
mean = np.mean(Y)
var = np.var(Y)
demiLargeurIC = 1.96*np.sqrt(Var_gY / N)
############################################

print("Estimateur MC \n")

print("Esp_gY = %1.3f Var_gY = %1.3f" %(Esp_gY, Var_gY))
print("mean = %1.3f  var = %1.3f" %(mean,var))
print("Intervalle de confiance 95%% pour E[g(Y)] = [ %1.3f , %1.3f ] \n" %(mean - demiLargeurIC, mean + demiLargeurIC))
print("erreur relative = %1.3f" %(demiLargeurIC/mean))

############################################
## Trajectoires de la moyenne empirique
############################################
M = 10

############################################
# Evaluer M trajectoires de l'estimateur empirique I_n
X = 2.0*np.random.rand(M,N)-1.0
Y = np.exp(X)
I_n =  np.cumsum(Y, axis=1)/integers1toN
############################################

# Affichage des trajectoires
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(integers1toN, I_n.T, color="b")

ax.set_xlim(0, N)
ax.set_ylim(1.0, 1.3)
ax.axhline(Esp_gY, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()