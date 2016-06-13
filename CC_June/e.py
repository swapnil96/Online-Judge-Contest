'''
     
    if a[0] % 2 == 0:
    	sum1 = 0
    	for j in xrange(a[0], a[1],  -2):
    		sum1 += ncr(a[0], j)
    					
    		return (2**(a[0] - 1) - sum1)
    				
    	else:	
'''
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

MOD = (10**9 + 7)
'''
def third():

    fact = []
    ifact = []
    fact.append(1)
    ifact.append(1)
    #fact[0] = ifact[0] = 1
    for i in range(1, 10001):
        
        fact.append((i * fact[i - 1]) % MOD)
        gc.disable()
        ifact.append(mesq(fact[i],(MOD - 2),MOD))
        #gc.enable()
    gc.enable()
    #print  (ifact, fact)
    return (fact, ifact)
'''
def third():

    inv = [1]*100001
    for i in xrange(2, 100001):
        inv[i] = MOD - ((MOD/i)*inv[MOD%i]%MOD)

    fact = [1]*100001
    fact_inv = [1]*100001
    for i in xrange(1, 100001):
        fact[i] = (fact[i-1]*i) % MOD
        fact_inv[i] = (fact_inv[i-1]*inv[i])%MOD    
        
    return  fact, fact_inv

fact1, fact_inv1 = third()

def NCR(X, Y):
    #return (fact1[X] * ifact1[X-Y] * ifact1[Y]) % MOD
    return (((fact1[X] * fact_inv1[Y]) % MOD) * fact_inv1[X-Y]) % MOD
     
def find(a, b):

    if b.count(0) > 0:
        #print 'asdf', b, b.count(0)
        a[0] -= b.count(0)     
        if a[1] >= a[0]:
            #print 'asdf'
            return 2**(a[0]) % MOD

        else:  
            
            sum1 = 0
            for i in xrange(a[1] + 1):
                sum1 += NCR(a[0], i)

            return sum1
            '''
            sum1 = 1
            nCi = 1 # i=0
            for i in xrange(1, a[1] + 1):#i = 1 to r-1
                sum1 += nCi
                nCi *= (a[0] - i + 1);
                nCi /= i

            return sum1# %= M;
            '''

    if a[1] == a[0]:
        return 2**(a[0] - 1) % MOD           

    if a[1] > a[0]:
    	if a[0] % 2 == 0 and a[1] % 2 == 0:
    		a[1] = a[0]
     
    	elif a[0] % 2 == 0 and a[1] % 2 != 0:
    		a[1] = a[0] - 1
     
    	elif a[0] % 2 != 0 and a[1] % 2 == 0:
    		a[1] = a[0] - 1
     
    	else:
    		a[1] = a[0]			
     
    if a[1] % 2 == 0:
        sum1 = 0
        for j in xrange(0, a[1] + 1, 2):
            sum1 += NCR(a[0], j)
    	    
    	return sum1
        
    else:
    	sum1 = 0
    	for j in xrange(1, a[1] + 1, 2):
            sum1 += NCR(a[0], j)
    	    #print ncr(a[0], j), a[1]

        return sum1
'''    
def find1(a):
     
    if a[1] > a[0]:
        more = a[1] - a[0]
    
    if more > a[0]:
    	if more % 2 == 0:
    		more = a[0]
     
    	else:
    		more = a[0] - 1
    			 
    if more % 2 == 0 and a[0] % 2 == 0:
		sum1 = 0
    	for j in xrange(a[0] - more - 2, -1, -2):
    		sum1 += ncr(a[0], j)
     
    	return (2**(a[0] - 1) - sum1)
     
	elif more % 2 == 0 and a[0] % 2 != 0:
    	sum1 = 0
    	for j in xrange(a[0] - more - 2, 0, -2):
    		sum1 += ncr(a[0], j)
     
    	return (2**(a[0] - 1) - sum1)
     
    elif more % 2 != 0 and a[0] % 2 == 0:
    	sum1 = 0
    	for j in xrange(a[0] - more - 2, 0, -2):
    		sum1 += ncr(a[0], j)
     
    	return (2**(a[0] - 1) - sum1)
     
    else:
    	if a[1] % 2 == 0:
    		if a[1] > a[0]/2:
    			sum1 = 0
    			for j in xrange(a[0] - 1, a[1], -2):
    				sum1 += ncr(a[0], j)
    						
    			return sum1
    						
    	else:	
    		sum1 = 0
    		for j in xrange(0, a[1] + 1, 2):
    			sum1 += ncr(a[0], j)
    	
    		return sum1
'''

tt =int(raw_input())
sol = []
for i in xrange(tt):
    a = map(int, raw_input().split())
	
    b = map(int, raw_input().split())
    sol.append(find(a, b))
     
for i in xrange(tt):
    print sol[i] % MOD
