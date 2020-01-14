# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

theta = 2.

def densiteGaussienne(x):
    return np.exp(-x*x/2.) / np.sqrt(2.*np.pi)

############################################
# Calculer moyenne et variance theoriques
# de l'estimateur d'importance avec quadrature
# numerique (par ex. scipy.integrate.quad )

# Moyenne et variance theoriques de l'estimateur d'importance 
Esp_g_theta = ???? 
Var_g_theta = ????
 
print("Esp_g_theta = %1.4f  Var_g_theta = %1.6f \n" %(Esp_g_theta, Var_g_theta))

N = 2000 # Taille echantillon

integers1toN = np.arange(1,N+1)

############################################
# Completer avec N tirages de la loi gaussienne
# centree en theta=2
# et avec le calcul de  l'estimateur d'importance
J_N = ????

# variance empirique et Intervalle de confiance
var = ????
demiLargeurIC = ????

print("Jmean = %1.4f  Jvar = %1.6f" %(J_N, var))
print("Intervalle de confiance 95%% pour E[g(Y)] = [ %1.6f , %1.6f ]" %(J_N - demiLargeurIC, J_N + demiLargeurIC))
print("erreur relative = %1.4f" %(demiLargeurIC/J_N))

################################################
# Trajectoires de l'estimateur empirique
################################################
M = 10

################################
# Completer avec M tirages de l'estimateur d'importance
# J_n pour n = 1,...,N
I_n = ?????

# Affichage des 10 trajectoires
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(integers1toN, I_n.T, color="b")

ax.set_xlim(0, N)
ax.set_ylim(0, 4*Esp_g_theta)
ax.axhline(Esp_g_theta, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()