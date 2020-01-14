import numpy as np
import matplotlib.pyplot as plt

N = 3000
X = np.random.exponential(0.5, N)

esp = 0.5
var = 0.25

################################################
## Question (b): completer avec le calcul d'une
## realisation de la suite des erreurs normalisees
## et son affichage 
################################################
integers1toN = np.arange(1,N+1)
moyenneEmp_N = np.cumsum(X)*1./integers1toN
err = np.sqrt(N/var)*(moyenneEmp_N - esp)

plt.figure()
plt.plot(integers1toN, err, color="b", label="la serie e_n")
plt.show()



