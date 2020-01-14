import numpy as np
import matplotlib.pyplot as plt

N = 1000
U = np.random.rand(N)

a = 1.
################################################################################
# L'inverse de la fonction de repartition d'une
# loi de Cauchy avec parametre a :
# F^{-1}(x) = a*tan(pi*(x-1/2))
########################################
X = a * np.tan(np.pi*(U-1./2))

integers1toN = np.arange(1,N+1)

moyenneEmp = np.cumsum(X) / integers1toN

plt.plot(integers1toN, moyenneEmp, color="b", label="Moyenne empirique")
plt.show()