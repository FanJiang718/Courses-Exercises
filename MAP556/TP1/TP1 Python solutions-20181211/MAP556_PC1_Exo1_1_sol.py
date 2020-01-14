import numpy as np
import matplotlib.pyplot as plt

N = 1000 #Nombre de tirages
X = np.random.rand(N) #Tirages independants de la loi uniforme sur [0,1]

#####################################
# But: calculer la suite des moyennes
# empiriques pour n de 1 a N

#####################################
## Calcul de la moyenne empirique:
## avec une boucle
#####################################
sumEmp = X[0]

moyenneEmp = X[0] * np.ones(N)

for i in range(1,N):
    sumEmp = sumEmp + X[i]
    
    moyenneEmp[i] = sumEmp / (i+1)

######################################
### Calcul de la moyenne empirique:
### avec des fonctions numpy
######################################
integers1toN = np.arange(1,N+1) #Un array contenant les entiers de 1 a N

moyenneEmp = np.cumsum(X) / integers1toN 

######################################
## Affichage
######################################
plt.plot(integers1toN, moyenneEmp, color="b", label="Moyenne empirique")

plt.axhline(0.5, color="r", label="Esperance")

plt.legend(loc="best")

plt.show()