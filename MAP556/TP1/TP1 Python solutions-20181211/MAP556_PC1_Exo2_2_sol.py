import numpy as np

N = 1000
X = np.random.rand(N)
esp = 0.5

moyenneEmp = np.sum(X) / N

moyenneCarres = np.sum(X*X)/N

varianceEmp = moyenneCarres - moyenneEmp*moyenneEmp

demiLargeurIC = 1.96*np.sqrt(varianceEmp)/np.sqrt(N)

print("esperance: %1.4f \n" %esp)
print("moyenne empirique: %1.4f \n" %moyenneEmp)

print("IC a 0.95: [%1.4f, %1.4f] \n" %(moyenneEmp-demiLargeurIC, \
                                       moyenneEmp+demiLargeurIC) )

print("erreur relative*100: %1.4f" %(demiLargeurIC/moyenneEmp * 100) )