# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# densite Gaussienne standard
def densiteGaussienne (x) :
    return np.exp(-x**2./2.) / np.sqrt(2.*np.pi)

# fonction g
def g(x):
    return np.maximum(x-2.,0.)

############################################
# Calculer E[g(Y)] et Var[g(Y)] avec quadrature
# numerique (par ex. scipy.integrate.quad )
Esp_gY = ?????
Var_gY = ?????

print("Esp_gY = %1.5f  Var_gY = %1.4f \n" %(Esp_gY,Var_gY))

N = 1000 # Taille echantillon

integers1toN = np.arange(1,N+1) # Un vecteur contenant les entiers de 1 a N

############################################
# Completer avec N tirages de la loi gaussienne
# centree reduite
Y = ?????

# On calcule la fonction g(Y) sur l'echantillon
GY = ?????

############################################
# Stocker dans 'mean' l'estimation MC de E[g(Y)]
# dans 'var' la variance empirique 
# et dans 'demiLargeurIC' la demi-largeur de l'intervalle de confiance 
# asymptotique a 95% pour E[g(Y)]
mean = ?????
var = ?????
demiLargeurIC = ?????

print("mean = %1.4f  var = %1.4f" %(mean,var) )
print("Intervalle de confiance 95%% pour E[g(Y)] = [ %1.4f , %1.4f ] \n" %(mean - demiLargeurIC, mean + demiLargeurIC))
print("erreur relative = %1.4f" %(demiLargeurIC/mean))

################################################
# Trajectoires de la moyenne empirique
################################################
M = 10 # Nombre de repetitions 

################################
# Evaluer les M tirages de l'estimateur empirique
# I_n pour n=1,...,N
I_n = ?????

################################
# Affichage des trajectoires
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(integers1toN, I_n.T, color="b")

ax.set_xlim(0, N)
ax.set_ylim(0, 4*Esp_gY)
ax.axhline(Esp_gY, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()