import time
from numpy import sum
from scipy.special import factorial
from scipy.stats import hypergeom
import matplotlib.pyplot as plt

#Q1 = input('What is K?')
#ans = int(Q1)

### create arrays to store "by hand" data and "library data"
t0_fac = time.time()
#fac_n=factorial(6123, exact=True)
#t1_fac = time.time()
#time = t1_fac - t0_fac
#print(time)

N = 50
K = 5
n = 10
k = 4

fac_n = 0
fac_k = 0
fac_N = 0
fac_K = 0
fac_Kk = 0
fac_NK = 0
fac_nk = 0
a = 0
fac_a = 0
fac_Nn = 0
hyp_fac = 0
hyp_fac_1 = 0
hyp_fac_2 = 0
hyp_fac_3 = 0
hyp_fac_prob = 0


for i in range(0,50):
    for j in range(i+1,50):
        ### compute hypergeometric distribution 
        ### "by hand" with factorials using 
        fac_n = factorial(n, exact=True)
        fac_k = factorial(k, exact=True)
        fac_N = factorial(N, exact=True)
        fac_K = factorial(K, exact=True)
        fac_Kk = factorial((K-k), exact=True)
        fac_NK = factorial((N-K), exact=True)
        fac_nk = factorial((n-k), exact=True)
        a = ((N-K)-(n-k))
        fac_a = factorial(a, exact=True)
        fac_Nn = factorial((N-n), exact=True)
        
        ### for the factorial of the number n
        ### store to variable hyp_fac
        ### store hyp_fac to the nth, kth element of your "by hand" array
        hyp_fac = (fac_n, fac_k)
        #print(hyp_fac)
        hyp_fac_1 = (fac_K/(fac_k*fac_Kk))
        hyp_fac_2 = (fac_NK/(fac_nk*fac_a))
        hyp_fac_3 = (fac_N/(fac_n*fac_Nn))
        hyp_fac_prob = sum((hyp_fac_1*hyp_fac_2)/hyp_fac_3)
        print(hyp_fac_prob)    


t1_fac = time.time()


total_by_hand = t1_fac-t0_fac
print(total_by_hand)

#t0_lib = time.time()
#N = 1000
#for n in range(0,300):
    #for k in range(n+1,500):
        ### compute hypergeometric distribution using the library function
	#y = np.arrange(0, n+1)
	#prb = hypergeom.cdf(y, K, n, N)
	#hyp_lib = hypergeom.rvs(K, n, N, size=10)
	#print(hyp_lib)     
	### store to variable hyp_lib
        ### hyp_lib = (call hypergeometric distribution function here!)
        ### store hyp_lib to the nth, kth element of your "lib" array
        #a = n*k
        
#t1_lib = time.time()   
#total_lib = t1_lib = t0_lib     
### print out both the "by hand" array and the "library" array to confirm they agree
### print out
