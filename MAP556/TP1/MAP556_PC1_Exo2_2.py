import numpy as np

N = 1000
X = np.random.rand(N)
esp = 0.5
delta = 1.96

moyenneEmp = np.sum(X) / N

################################################################
# Stocker dans la variable 'moyenneCarres' la moyenne empirique
# des carres de X
#
moyenneCarres = np.sum(X*X)/N
#
# Stocker dans la variable 'varianceEmp' la variance empirique
# et dans 'demiLargeurIC' la demi largeur de l'intervalle de 
# confiance a 95%
#
varianceEmp = moyenneCarres - moyenneEmp**2
# 
demiLargeurIC = delta * np.sqrt(varianceEmp/N)
# 
########

print("esperance: %1.4f \n" %esp)
print("moyenne empirique: %1.4f \n" %moyenneEmp)

print("IC a 0.95: [%1.4f, %1.4f] \n" %(moyenneEmp - demiLargeurIC, \
                                       moyenneEmp + demiLargeurIC) )

print("erreur relative*100: %1.4f" %(demiLargeurIC/moyenneEmp * 100) )