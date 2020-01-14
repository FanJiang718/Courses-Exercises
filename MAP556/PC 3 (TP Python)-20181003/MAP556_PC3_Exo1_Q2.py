# -*- coding: utf-8 -*-
print("-" * 40)
print("TP3 Exo 1 Question 2")
print ("-" * 40) 

print("Estimation avec variable de controle \n")

import numpy as np
import matplotlib.pyplot as plt

N = 1000 # Taille echantillon

integers1toN = np.arange(1,N+1) # Un vecteur contenant les entiers de 1 a N

############################################
# Calculer la valeur exacte de m_r
m_r = 1.5
############################################

############################################
# Simuler les echantillons de valeurs de Y
# et de Y_controle
U = np.random.rand(N)
Y = np.exp(U)

Ycontrole = Y-(1 + U) + m_r
############################################

############################################
## Calculer les deux estimateurs, leurs
## variances empiriques, et les demi-largeurs
## des intervalles de confiance

Mean_MC = np.mean(Y)
Variance_MC = np.std(Y)**2

Mean_controle = np.mean(Ycontrole)
Variance_controle = np.std(Ycontrole)**2

demiLargeurIC95_MC = 1.96*np.sqrt(Variance_MC/N)
demiLargeurIC95_Contr = 1.96*np.sqrt(Variance_controle/N)

############################################
# Gain en termes de nombre de simulations
# pour la meme precision

gain_controle = Variance_MC/Variance_controle
############################################

############################################
# Pour l'affichage: valeur exacte de E[g(Y)]
Esp_gY = np.exp(1.) - 1.

print("Taille echantillon = %d" %N)
print("Esp_gY = %1.3f \n" %Esp_gY)

print("Estimateur MC : moyenne= %1.3f  variance emp = %1.3f" \
      %(Mean_MC, Variance_MC))
print("IC(95%%) = [%1.3f,%1.3f] \n" \
      %(Mean_MC-demiLargeurIC95_MC, Mean_MC+demiLargeurIC95_MC))

print("Estimateur Controle : moyenne= %1.3f  variance emp = %1.3f" \
      %(Mean_controle, Variance_controle))
print("IC(95%%) = [%1.3f,%1.3f] \n" \
      %(Mean_controle-demiLargeurIC95_Contr, Mean_controle+demiLargeurIC95_Contr))

print("Gain en nombre de simulations avec variable de controle : %1.2f" %gain_controle)

############################################
## Affichage de 10 trajectoires 
############################################

############################################
# Simuler M=10 trajectoires des estimateurs
# I_n et I_n^c
# Taille souhaitee pour les arrays: M x N

M = 10

U = np.random.rand(M,N)
Y = np.exp(U)
Ycontrole = Y-(1 + U) + m_r

I_n = np.cumsum(Y, axis =1)/ integers1toN

Ic_n = np.cumsum(Ycontrole, axis =1)/ integers1toN

############################################
## On affiche les 10 trajectoires
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(integers1toN, I_n[0], color="b", label="MC")
ax.plot(integers1toN, I_n[1:].T, color="b")

ax.plot(integers1toN, Ic_n[0], color="g", label="Controle")
ax.plot(integers1toN, Ic_n[1:].T, color="g")
ax.axhline(Esp_gY, color="r", label="Esperance")

ax.set_xlim(0, N)
ax.set_ylim(1.4, 2.2)
ax.legend(loc="best")
plt.show()

