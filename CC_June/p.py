#from math import *
import math
#from operator import mul
try:
    rng = xrange
except NameError:
    rng = range  # Python 3+

def mesq(base, exp, mod, debug=False):
    """Modular exponentiation by squaring."""
    result, counter = 1, 0
    cache = (counter, base % mod)
    while exp:
        leap = 1
        if exp & 1:
            current = cache[1]
            for x in rng(counter - cache[0]):
                current = pow(current, 2) % mod  # pow() is fast!
            cache = (counter, current)
            result = (result * current) % mod
        else:
            # In case of many zeros, this will give a small speedup:
            while not exp & ((1<<(leap*2))-1):
                leap *= 2
        counter += leap
        exp >>= leap
    return result

n = int(raw_input())
que = map(int, raw_input().split())
que1 = [0]*n
query = int(raw_input())
MOD = 10**9 + 7
for i in xrange(n):
    que1[i] = math.log10(que[i])
    que[i] = que[i]/(10**5.0)

def find(no):

    sum1 = sum(que1[0::no])
    pro = 1
    for i in xrange(0, n, no):
   		#sum1 += que1[i]
    	#pro = 10**que1[i]
        pro = ((pro % MOD)*que[i]) % MOD
       #pro = ((pro % MOD)*(int(10**que1[i]))) % MOD

     
    if sum1 <= 8:
    	pro = int(round(10**(sum1), 2))
    	#print round(10**v, 8), 10**(int(sum1))
    	return ((str(pro)[0]), int(pro % MOD))
    	
    inte = int(sum1)   
    fra = sum1 - int(sum1)
    #pro = (mesq(10, int(sum1), MOD) * (10**(v)))%MOD
    #fra = sum1 - int(sum1)
    pro = (pow(10, 5*n , MOD) * (pro % MOD)) % MOD
    #print round(10**v, 8), 10**(int(sum1))
    got = 10**(fra+5)
    got = round(got, 2)
    return ((str(got)[0]), int(pro % MOD))

sol = []
k = 0
for i in xrange(query):
    a = map(int, raw_input().split())
    if a[0] == 1:
        que1[a[1] - 1] = math.log10(a[2])
        que[a[1] - 1] = a[2]

    else:
        k += 1
        sol.append(find(a[1]))

for i in xrange(k):
	print ' '.join(map(str, sol[i]))

