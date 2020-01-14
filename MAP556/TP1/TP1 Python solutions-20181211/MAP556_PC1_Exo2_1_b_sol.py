import numpy as np
import matplotlib.pyplot as plt

N = 3000
X = np.random.exponential(0.5,N)

esp = 0.5
var = 0.25

################################################
## Question (b): completer avec le calcul d'une
## realisation de la suite des erreurs normalisees
## et son affichage 
################################################
integers1toN = np.arange(1,N+1)

moyenneEmp = np.cumsum(X) / integers1toN

erreurNormalisee = (moyenneEmp - esp) * np.sqrt(integers1toN / var)

plt.plot(integers1toN, erreurNormalisee, color="b", label="erreur normalisee")
plt.legend(loc="best")

