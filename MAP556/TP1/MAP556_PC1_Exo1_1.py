import numpy as np
import matplotlib.pyplot as plt

N = 1000 #Nombre de tirages

########
# Completer avec N tirages de la loi uniforme sur [0,1]
#
X = np.random.rand(N) 
#
########

integers1toN = np.arange(1,N+1) #Un array contenant  les entiers de 1 a N

############
# Stocker dans la variable 'moyenneEmp' la suite de moyennes empiriques
# pour n allant de 1 a N
#
moyenneEmp = np.cumsum(X) * 1./integers1toN
#
############

############
#Affichage
############
plt.plot(integers1toN, moyenneEmp, color="b", label="Moyenne empirique")

plt.axhline(0.5, color="r", label="Esperance")

plt.legend(loc="best")
plt.show()
