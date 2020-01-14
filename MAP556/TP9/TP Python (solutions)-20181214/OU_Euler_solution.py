import numpy as np
import matplotlib.pyplot as plt

T = 1. 
sig = 0.8
a = 0.5 
m = 90.
x0 = 100.
    
def erreurForteEuler(T, sig, a, m, x0, N, M):
    """
    Estimation de l'erreur forte du schema d'Euler de pas h=T/N
    a partir d'un echantillon de M simulations.
    
    Output: le couple (erreur forte, demi-largeur de l'IC a 95%)
    """
    X = x0 * np.ones(M)
    Xe = x0 * np.ones(M)
    max_er = np.zeros(M)
    
    ########################
    # Parametres utiles pour
    # la discretisation
    ########################
    a_m_delta_T = a * m * T/N
    drift_X = m * (1 - np.exp(-a*T/N))

    ########################
    # Matrice de covariance
    ########################
    var_int_stoch = (1 - np.exp(-2*a*T/N)) / (2*a)
    var_increm_brownien = T/N
    covar = (1 - np.exp(-a*T/N)) / a
    
    C = np.array([[var_int_stoch, covar],[covar, var_increm_brownien]])
    
    L = np.linalg.cholesky(C)
    
    for k in range(N):
        g = np.random.randn(2,M)
        
        increments_joints = np.dot(L,g)
        
        ##############################
        # Processus X
        ##############################
        X = np.exp(- a*T/N) * X  \
            + drift_X \
            + sig * increments_joints[0,:]
        ##############################
        # Schema d'Euler Xe
        ##############################
        Xe = Xe*(1. - a*T/N) + a_m_delta_T + sig * increments_joints[1,:]
        
        max_er = np.maximum(max_er, (X-Xe)**2)
    
    err_quadratique_eul = np.sum(max_er) / M
    
    err_eul = np.sqrt(err_quadratique_eul)
    
    ##############################
    # IC d'apres la methode delta
    ##############################
    variance_delta_methode = np.var(max_er) / (4. * err_quadratique_eul)

    largeur_IC_eul = 1.96 * np.sqrt(variance_delta_methode/M)
    
    return err_eul, largeur_IC_eul


M = int(1.e3) #nombre de simulations independantes
N = 1 #nombre initial de pas de discretisation

P = 6

Npas = np.zeros(P)

err_eul = np.zeros(P) #pour stocker les erreurs du schema d'Euler
largeur_IC_eul = np.zeros(P) #pour stocker les largeurs des IC 

for i in range(P):
    Npas[i] = N
    
    err_eul[i], largeur_IC_eul[i] = erreurForteEuler(T, sig, a, m, x0, N, M)

    N = 2*N #multiplication du nombre N de pas par 2    

###################################
# Representation graphique de l'erreur
# forte en fonction du pas h=T/N
###################################
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