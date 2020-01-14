import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from time import time 
import scipy.stats as sts

## Parametres
K = 1.2
x0 = 1.
sigma = 0.2

T2 = 2.
T1 = T2 / 2.

M = int(5e3)

###################################################
## Q1 (a): formule explicite
##         pour l'esperance conditionnelle 
###################################################

def putBlackScholes(x_0, T1, T2, K, W1, sigma):
    """
    Prix en T1 du Put Black-Scholes de maturite T2
    en fonction de la valeur courante du mouv Brownien en T1.
    
    Soit: la fonction v_1(W1) de la question 1.(a)
    
    W1: un array numpy, contenant les valeurs courantes
    du mouv Brownien en T1
    """
    sigmaSqrtDeltaT = sigma*np.sqrt(T2 - T1)
    
    ######################################
    # TO DO: coder la formule explicite
    ## pour la fonction P_BS
    ######################################
    x = x_0*np.exp(-0.5*sigma*sigma*T1+sigma*W1)
    d2 = np.log(x/K)/sigmaSqrtDeltaT-0.5*sigmaSqrtDeltaT
    d1 = d2 + sigmaSqrtDeltaT
    P = K*norm.cdf(-d2) - x* norm.cdf(-d1)
    ## Output: un array de la meme taille que W
    return P
#print(putBlackScholes(x0,T1,T2,K,0,sigma))
###################################################
## On genere les tirages gaussiens et on construit
## le MB et le MBG aux deux instants T1 et T2
###################################################
def MBG(x0, T, sigma, W):
    """
    Mouvement Brownien geometrique a l'instant T, de parametre de 
    volatilite sigma, a partir de la valeur du mouvement Brownien W
    """
    return x0 * np.exp(-0.5*sigma*sigma*T + sigma * W)

time0 = time()

#################################################
## TO DO: Remplacer W1,W2 avec un echantillon de ;
## tirages du mouvement Brownien aux dates T1 et
## T2 et X1, X2 avec le MBG correspondant
W1 = np.random.randn(M)*np.sqrt(T1); W2 = W1 + np.random.randn(M)*np.sqrt(T2-T1)
X1 = MBG(x0,T1,sigma,W1); X2 = MBG(x0,T2,sigma,W2)
################################################

time0_1 = time()

timeSimulations = time0_1 - time0

###################################################
### 1. Prix Benchmark
###################################################

time1 = time()

v_1 = putBlackScholes(x0, T1, T2, K, W1, sigma)

################################################
## TO DO: completer avec le calcul du prix
## benchmark u_0^M et l'estimation de la variance
## asymptotique de l'estimateur
prix_benchmark = np.maximum(max(K-x0,0),np.mean(np.maximum((K-X1)*((K-X1)>0),v_1)))
var_MC = np.var(np.maximum((K-X1)*((K-X1)>0),v_1))
################################################

rayonIC = 1.96 * np.sqrt(var_MC/M)

time2 = time()

print("Prix benchmark = %1.4f +/- %1.4f" %(prix_benchmark, rayonIC) )
print("Erreur relative (TCL) = %1.3f" %(rayonIC / prix_benchmark) )
print("Time: %1.4f \n" %(time2 - time1 + timeSimulations) )

###################################################
### 2. Prix par regression empirique
###################################################

##################################
### On genere les cellules I_k
##################################
a = 3.*np.sqrt(T1)

n = int(M**(1./3))

intervals = np.linspace(-a, a, n+1)

##################################
## On genere les coefficients de 
## regression empirique 
##################################
def coeffsRegressionEmpirique(W1, W2, intervals, T2, K, x0, sigma):
    step = intervals[1] - intervals[0]
    alpha = np.zeros(intervals.size - 1)
    
    for k, leftPoint in enumerate(intervals[:-1]):
        
         insideCell = np.logical_and( leftPoint <= W1, W1 < leftPoint+step )         
         
         MBG_T2 = MBG(x0, T2, sigma, W2[insideCell])
         
         #############################################
         ## TO DO: Completer avec le calcul des
         ## coefficients alpha[k]
         #############################################
         alpha[k] = np.sum(((K-MBG_T2)>0)*(K-MBG_T2))/np.sum(insideCell)
         
    return alpha

time3 = time()

alpha = coeffsRegressionEmpirique(W1, W2, intervals, T2, K, x0, sigma)

def returnIndex(w1,intervals):
    """
    Fct qui renvoie l'indice de la cellule I_k contenant w1.
    Renvoie -1 si w1 n'est contenu dans aucune cellule.
    
    But: calculer ci-dessous approx_empirique_T1 = v_1(W1)
    
    ATTENTION:    
    parametre w1 -> un float ou un double (cette fct ne gere pas les array)
    """
    if np.logical_or( (w1 < intervals[0]).all(), (w1 > intervals[-1]).all() ):
        return -1
    else:
        index =  np.max( np.argwhere(intervals <= w1) )
        return index

################################################
## TO DO: Completer avec le calcul
## - De l'approximation empirique v_1_tilde(W1)
##   dans l'array approx_empirique_T1
## - Du prix par regression empirique u_tilde_0^M 
##
approx_empirique_T1 = np.zeros(M)
for i in range(M):
    approx_empirique_T1[i] = alpha[returnIndex(W1[i],intervals)]

u1 = np.maximum(((K-X1)>0)*(K-X1), approx_empirique_T1)
prix_RegrEmp = np.maximum(((K-x0)>0)*(K-x0),np.mean(u1))
################################################

time4 = time()

print("Prix par regression empirique = %1.4f" %prix_RegrEmp)
print("Time: %1.4f \n" %(time4 - time3 + timeSimulations))

######################################
## On peut afficher la vraie fonction
## v_1 et son approximation empirique
## pour comparaison
#####################################
x = np.linspace(-a, a, 100)

u_exact = putBlackScholes(x0, T1, T2, K, x, sigma)

plt.plot(x, u_exact, color="b", label="$v_1$")
plt.step(intervals, np.append(alpha, alpha[-1]), where="post", color="r", label=r"$\tilde{v}_1$")
plt.xlabel("valeurs de $W_1$", fontsize=17)
plt.legend(loc="best", fontsize=20)

###################################################
### 3. Prix Longstaff-Schwartz
###################################################
time5 = time()

def tempsArretOptimal(X1, X2, u_1_tilde):
    ## On reutilise l'approximation empirique definie
    ## plus haut, correspondant a u_1_tilde
    gain_T1 = np.maximum(K - X1, 0.)
    
    mean_0 = np.mean(u_1_tilde)
    
    if np.maximum((K-x0), 0.) >= mean_0:
        return np.zeros(M)
    else:
        tau = 1 * (u_1_tilde <= gain_T1) \
              + 2 * (u_1_tilde > gain_T1)
    
    return tau

###################################################
## To Do: completer avec le calcul
## - du temps d'arret optimal tau (echantillon tau_m)
## - de l'estimateur Longstaff-Schwartz du prix
##
tau = tempsArretOptimal(X1,X2,u1)
Schwartz = np.zeros(M)
for i,t in enumerate(tau):
    if t ==0:
        Schwartz[i] = np.maximum(K-x0,0)
    elif t == 1:
        Schwartz[i] = np.maximum(K-X1[i],0)
    else:
        Schwartz[i] = np.maximum(K-X2[i],0)
mean_LongSchwartz = np.mean(Schwartz)
###################################################

time6 = time()

print("Prix Longstaff-Schwartz = %1.4f" %mean_LongSchwartz)
print("Time: %1.4f \n" %(time6 - time5 + time4 - time3 + timeSimulations))

###################################################
#### 4. Prix "simulations dans les simulations"
###################################################

###################################################
## On genere M tirages de X2 pour chaque valeur
## dans l'echantillon X1.
## Il faudra repeter les tirages de M gaussiennes iid 
## POUR CHAQUE valeur de X1.
###################################################
u_0 = 0.
u_0_carre = 0.

time7 = time()

for m, w1 in enumerate(W1):
    G = np.random.randn(M)
    
    ###################################################
    ## To Do: completer avec
    ## - les tirages de W_2 conditionnellement a W1=w1
    ## - la mise a jour de la somme des contributions au
    ##   prix u_0
    ## - la mise a jour de la somme des carres
    W2 = w1 + np.sqrt(T2-T1)* G
    v1 = np.mean(np.maximum(K-x0*np.exp(-0.5*sigma*sigma*T2+sigma*W2),0))
    u_0 += np.maximum(np.maximum(K-X1[m],0), v1)
    u_0_carre += np.maximum(np.maximum(K-X1[m],0), v1)**2
    ###################################################

var_sim_dans_sim = u_0_carre/M - u_0*u_0/(M*M)

u_0 = np.maximum( np.maximum(K-x0,0.), u_0/M )

rayonIC_sim_2 = 1.96 * np.sqrt(var_sim_dans_sim/M)

time8 = time()

print("Prix par MC de MC = %1.4f" %u_0, " +/- %1.4f" %rayonIC_sim_2)
print("Erreur relative = %1.3f \n" %(rayonIC_sim_2 / u_0) )
print("Time: %1.4f" %(time8 - time7), "\n")