# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 3 Question 2")
print("-" * 40)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

theta = 2.

def densiteGaussienne(x):
    return np.exp(-x*x/2.) / np.sqrt(2.*np.pi)

def g_importance(z, theta=theta):
    return np.maximum(z-2.,0.) * np.exp(-theta*z + theta*theta/2.)

def integrandEsperance(z, theta=theta):
    return densiteGaussienne(z-2.0) * g_importance(z,theta)

def integrandMomentOrdre2(z, theta=theta):
    return densiteGaussienne(z-2.0)* g_importance(z,theta)**2

# Moyenne et variance theoriques de l'estimateur d'importance 
Esp_g_theta = quad(integrandEsperance, -100., 100.)[0] 
Esp_2 = quad(integrandMomentOrdre2, -100., 100.)[0]
Var_g_theta = Esp_2 - Esp_g_theta*Esp_g_theta
 
print("Esp_g_theta = %1.4f  Var_g_theta = %1.6f \n" %(Esp_g_theta, Var_g_theta))

N = 2000 # Taille echantillon

integers1toN = np.arange(1,N+1)

Z = np.random.randn(N) + theta # Loi gaussienne centrée en theta=2

GY = np.maximum(Z-2.,0.) * np.exp(-theta*Z + theta*theta/2.)

# estimateur d'importante
mean = np.mean(GY)

# variance empirique et Intervalle de confiance
var = np.var(GY)
demiLargeurIC = 1.96 * np.sqrt(Var_g_theta / N)

print("Jmean = %1.4f  Jvar = %1.6f" %(mean, var))
print("Intervalle de confiance 95%% pour E[g(Y)] = [ %1.5f , %1.5f ]" %(mean - demiLargeurIC, mean + demiLargeurIC))
print("erreur relative = %1.3f" %(demiLargeurIC/mean))

################################################
# Trajectoires de l'estimateur empirique
################################################
M = 10

Z = np.random.randn(M,N) + theta # Loi gaussienne centrée en theta=2

GY = np.maximum(Z-2.,0.) * np.exp(-theta*Z + theta*theta/2.)

I_n = np.cumsum(GY, axis=1)/ integers1toN

# Affichage des 10 trajectoires
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(integers1toN, I_n.T, color="b")

ax.set_xlim(0, N)
ax.set_ylim(0, 4*Esp_g_theta)
ax.axhline(Esp_g_theta, color="r", label="Esperance")
ax.legend(loc="best")
plt.show()