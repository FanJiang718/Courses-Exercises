import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from time import time 

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

def putBlackScholes(x0, T1, T2, K, W, sigma):
    """
    Prix en T1 du Put Black-Scholes de maturite T2
    en fonction de la valeur courante du mouv Browien en T1.
    
    Soit: la fonction v_1(W1) de la question 1(a)
    
    W1: un array numpy, qui contiendra les valeurs courantes
    du mouv Brownien en T1
    """
    sigmaSqrtDeltaT = sigma*np.sqrt(T2 - T1)
    
    ln_x = np.log(x0) + sigma*W - 0.5*sigma*sigma*T1
    
    d2 = (ln_x - np.log(K)) / sigmaSqrtDeltaT - 0.5*sigmaSqrtDeltaT
    d1 = d2 + sigmaSqrtDeltaT
    
    return  K*norm.cdf(-d2) - np.exp(ln_x)*norm.cdf(-d1)

###################################################
## On genere les tirages de W1 et W2 et on construit
## le processus X (mouvement Brownien geometrique)
## aux deux instants T1 et T2
###################################################
def MBG(x0, T, sigma, W):
    """
    Mouvement Brownien geometrique a l'instant T, 
    de valeur initial x_0, parametre de  volatilite sigma,
    a partir de la valeur du mouvement Brownien W
    """
    return x0 * np.exp(-0.5*sigma*sigma*T + sigma * W)

time0 = time()

G = np.random.randn(2,M)

W1 = np.sqrt(T1) * G[0,:]
W2 = W1 + np.sqrt(T2 - T1) * G[1,:]

X1 = MBG(x0, T1, sigma, W1)
X2 = MBG(x0, T2, sigma, W2)

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
## asymptotique 

gain_T1 = np.maximum(K - X1, 0.)

u_1 = np.maximum(gain_T1, v_1)

moyenne_emp_Y1 = np.mean(u_1)

prix_benchmark = np.maximum( np.maximum(K - x0, 0.), moyenne_emp_Y1 )

var_MC = np.var(u_1)

################################################
rayonIC = 1.96 * np.sqrt(var_MC/M)

time2 = time()

print("Prix benchmark = %1.4f +/- %1.4f" %(prix_benchmark, rayonIC))
print("Erreur relative (TCL) = %1.4f" %(rayonIC / prix_benchmark) )
print("Time: %1.4f \n" %(time2 - time1 + timeSimulations))

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
         
         numberInsideCell = MBG_T2.size
         
         if numberInsideCell != 0.:
             contributionToCell = np.maximum(K - MBG_T2, 0.)
             
             alpha[k] = np.sum(contributionToCell) / numberInsideCell
    
    return alpha

time3 = time()

alpha = coeffsRegressionEmpirique(W1, W2, intervals, T2, K, x0, sigma)

def returnIndex(w1, intervals):
    """
    Fct qui renvoie l'indice de la cellule I_k contenant w1.
    Renvoie -1 si w1 n'est contenu dans aucune cellule.
    
    ATTENTION:    
    parametre w1 -> un float ou un double (la fct ne gere pas les array)
    """
    if np.logical_or( w1 < intervals[0], w1 > intervals[-1] ):
        return -1
    else:
        index =  np.max( np.argwhere(intervals <= w1) )
        return index

####################################################
## TO DO: Completer avec le calcul
## - De l'approximation empirique v_1_tilde(W1)
##   dans l'array approx_empirique_T1
## - Du prix par regression empirique u_tilde_0^M 

approx_empirique_T1 = np.zeros(M)

for m, w in enumerate(W1):
    index = returnIndex(w, intervals)
    
    if index >= 0:
        approx_empirique_T1[m] = alpha[index]
## Pour les tirages W1 qui sont en dehors de l'union
## des cellules, on a bien v_1_tilde(W1) = 0

u_1_tilde = np.maximum(gain_T1, approx_empirique_T1)

mean_RegrEmp = np.mean(u_1_tilde)

prix_RegrEmp = np.maximum( np.maximum(K-x0,0.), mean_RegrEmp )

####################################################

time4 = time()

print("Prix par regression empirique = %1.4f" %prix_RegrEmp)
print("Time: %1.4f \n" %(time4 - time3 + timeSimulations))

######################################
## On peut afficher la vraie fonction
## v_1 et son approximation empirique
## pour comparaison
#####################################
x = np.linspace(-a, a, 100)

v_1_exact = putBlackScholes(x0, T1, T2, K, x, sigma)

plt.plot(x, v_1_exact, color="b", label="$v_1$")

plt.step(intervals, np.append(alpha, alpha[-1]), where="post", color="r", label=r"$\tilde{v}_1$")

plt.xlabel("valeurs de $W_1$ pour $T_1$=%1.1f" %T1, fontsize=17)
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
    
    if np.maximum((K-x0),0.) >= mean_0:
        return np.zeros(M)
    else:
        tau = 1 * (u_1_tilde <= gain_T1) \
              + 2 * (u_1_tilde > gain_T1)
    
    return tau

tau = tempsArretOptimal(X1, X2, approx_empirique_T1)

X = np.array([x0*np.ones(M), X1, X2])
X_tau = np.zeros(M)

for m, t in enumerate(tau):
    X_tau[m] = X[t,m]
    
echantillon = np.maximum(K - X_tau, 0.)

mean_LongSchwartz = np.mean(echantillon)

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
    
    W2 = w1 + np.sqrt(T2-T1)*G
    
    X2 = MBG(x0, T2, sigma, W2)
    
    v_hat_1 = np.mean( np.maximum(K - X2, 0.) )
    
    gain_T1 = np.maximum(K - MBG(x0, T1, sigma, w1), 0.)
    
    u_0 += np.maximum(gain_T1, v_hat_1)
    
    u_0_carre += np.maximum(gain_T1, v_hat_1)**2

var_sim_dans_sim = u_0_carre/M - u_0*u_0/(M*M)

u_0 = np.maximum( np.maximum(K-x0,0.), u_0/M )

rayonIC_sim_2 = 1.96 * np.sqrt(var_sim_dans_sim/M)

time8 = time()

print("Prix par Sim dans Sim = %1.4f +/- %1.4f" %(u_0, rayonIC_sim_2))
print("Erreur relative (TCL) = %1.4f" %(rayonIC_sim_2 /u_0) )
print("Time: %1.4f \n" %(time8 - time7))