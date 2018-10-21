import time
import numpy as np
from numpy import sum
from scipy.special import factorial


### reads data from text file, stores to array for access later
read_array=np.loadtxt("HS_Set.txt")
### opens a file to write data to  
f = open("test_calc.txt","w")

### initialize variables... doesn't really matter
### what values you give them, they will be assigned 
### when you loop over the entries of read_array
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


for i in range(0,len(read_array)):
    
        k = read_array[i][0]
        n = read_array[i][1]
        K = read_array[i][2]
        N = read_array[i][3]
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
        ### write the k, n, K, and N values along with hypergeometric dis. result
        ##  to the file you opened... first save data as a single string
        wstr = str(k)+","+str(n)+","+str(K)+","+str(N)+","+str(hyp_fac_prob)
        ### write that string to the file
        f.write(wstr)
        ### make a new line in the file so the data is formatted normally
        f.write('\n')
    

### now close the file you wrote to
f.closed



