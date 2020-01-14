import numpy as np
import matplotlib.pyplot as plt

N = 1000
U = np.random.rand(N)

a = 1.

########
# Stocker dans X des simulations de la loi de Cauchy de parametre a
# en utilisant l'inverse de la fct de repartition
#
X = a*np.tan(np.pi*(U-0.5))
#
########

integers1toN = np.arange(1,N+1)

########
# Calculer et stocker dans la variable 'moyenneEmp' la suite des moyennes empiriques
# 
moyenneEmp = 1./integers1toN * np.cumsum(X)
# 
# Afficher la suite à l'aide de la fonction plot de matplotlib.pyplot
#
plt.plot(integers1toN, moyenneEmp, color="b", label="Moyenne empirique")

#
########




