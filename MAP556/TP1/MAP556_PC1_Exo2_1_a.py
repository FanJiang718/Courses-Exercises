import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

N = 3000 #Nombre de tirages pour le calcul de la moyenne empirique
M = 5000 #Nombre de repetitions

####################################################
# Tirages independants de N*M v.a. exponentielles
# de parametre lambda=2
#
# ATTENTION: la fonction random.exponential reçois en premier argument
#  la moyenne 1/lambda de la distribution et non son parametre lambda
X = np.random.exponential(0.5, (N,M))
####################################################

esp = 0.5
var = 0.25

####################################################
# Stocker dans la variable 'moyenneEmp_N' un echantillon de M valeurs
# de la moyenne empirique Xbar_N
#
moyenneEmp_N = 1./N* np.sum(X,axis = 0)

#
# Stocker dans la variable 'erreurNormalisee_N' l'echantillon de M valeurs
# de l'erreur normalisee
#
erreurNormalisee_N = np.sqrt(N/var)*(moyenneEmp_N - esp)
########


#Affichage
plt.hist(erreurNormalisee_N, normed="True", bins=int(np.sqrt(M)), label="erreur normalisee")

x = np.linspace(-5,5,100)

####################################################
# Completer avec le calcul de la densite gaussienne centree reduite
# sur les abscisses x
#
densiteGaussienne = sts.norm.pdf(x)
#
########

plt.plot(x, densiteGaussienne, color="red", label="densite gaussienne")
plt.legend(loc="best")
