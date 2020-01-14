# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

T = 1. 
sig = 0.2
r = 0.05 
S0 = 100
    
def erreurForteEuler(T,sig,r,S0,N,M):
    """
    Estimation de l'erreur forte du schema d'Euler de pas h=T/N
    a partir d'un echantillon de M simulations
    
    Output: le couple (erreur forte, demi-largeur de l'IC a 95%)
    """
    S = S0*np.ones(M)
    Se = S0*np.ones(M)
    max_er = np.zeros(M)
    
    ########################
    # Parametres utiles pour
    # la discretisation
    ########################
    der = (r - sig*sig/2.) * T/N
    r_t = r * T/N
    sig_t = sig*np.sqrt(T/N)
    
    for k in range(N):
        g = np.random.randn(M)
        ##############################
        # Processus S
        ##############################
        S = S * np.exp(der + sig_t*g)
        ##############################
        # Schema d'Euler
        ##############################
        Se = Se * (1. + r_t + sig_t*g)
        
        max_er = np.maximum(max_er, (S-Se)**2)
    
    err_quadratique_eul = np.sum(max_er) / M
    
    err_eul = np.sqrt(err_quadratique_eul)
    
    ##############################
    # IC d'apres la methode delta
    ##############################
    variance_delta_methode = np.var(max_er) / (4. * err_quadratique_eul)

    largeur_IC_eul = 1.96 * np.sqrt(variance_delta_methode/M)
    
    return err_eul, largeur_IC_eul


M = int(1.e5) #nombre de simulations independantes
N = 1 #nombre initial de pas de discretisation

P = 6

Npas = np.zeros(P)

err_eul = np.zeros(P) #pour stocker les erreurs du schema d'Euler
largeur_IC_eul = np.zeros(P) #pour stocker les largeurs des IC 

for i in range(P):
    Npas[i] = N
    
    err_eul[i], largeur_IC_eul[i] = erreurForteEuler(T, sig, r, S0, N, M)

    N = 2*N #multiplication du nombre N de pas par 2    

#######################################
# Representation graphique de l'erreur
# forte en fonction du pas h=T/N
#######################################
plt.clf()
plt.plot(T/Npas, err_eul, color="r", label="Erreur forte")
plt.plot(T/Npas, err_eul-largeur_IC_eul, color="b", label="IC 95%")
plt.plot(T/Npas, err_eul+largeur_IC_eul, color="b")
plt.xlabel('Pas de discretisation')
plt.legend(loc="best")
plt.show()

#########################################
# On affiche les valeurs de l'erreur et
# de la largeur de l'IC
#########################################
print("N:"); print(Npas)
print("Erreurs du schema d'Euler de pas N:"); print(err_eul)
print("IC a 95%:"); print (largeur_IC_eul)