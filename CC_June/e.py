'''
     
    if a[0] % 2 == 0:
    	sum1 = 0
    	for j in xrange(a[0], a[1],  -2):
    		sum1 += ncr(a[0], j)
    					
    		return (2**(a[0] - 1) - sum1)
    				
    	else:	
'''
import math
def nCr(n,r):
    f = math.factorial

    return f(n)/ f(r) / f(n-r)
     
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
     
def find(a, b):

    if b.count(0) > 0:
        #print 'asdf', b, b.count(0)
        a[0] -= b.count(0)     
        if a[1] >= a[0]:
            #print 'asdf'
            return 2**(a[0])

        else:
            if a[1] > a[0] / 2:
                sum1 = 0
                for j in xrange(a[1]+1, a[0] + 1):
                    sum1 += ncr(a[0], j)

                return 2**(a[0]) - sum1

            else:    
                sum1 = 0
                for i in xrange(a[1] + 1):
                    sum1 += ncr(a[0], i)

                return sum1

    if a[1] == a[0]:
        return 2**(a[0] - 1)            

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
    	if a[1] > a[0]/2:
            
            sum1 = 0
            for j in xrange(a[1] + 2, a[0] + 1, 2):
                sum1 += ncr(a[0], j)
        
            return 2**(a[0] - 1) - sum1
            
            '''
            temp = ncr(a[0], a[1] + 2)
            #r = a[1] + 2
            sum1 = temp
            for j in xrange(a[1] + 2, a[0] - 1, 2):
                temp *= (((a[0] - j - 1)*(a[0] - j))/((j + 1)*(j + 2)))
                sum1 += temp
                #r += 2

            return 2**(a[0] - 1) - sum1   
            ''' 
             
        else:    
            
            sum1 = 0
            for j in xrange(0, a[1] + 1, 2):
                sum1 += ncr(a[0], j)
    	
    	    return sum1
            '''
            temp = ncr(a[0], 0)
            sum1 = temp
            for j in xrange(0, a[1] - 2, 2):
                temp *= (((a[0] - j - 1)*(a[0] - j))/((j + 1)*(j + 2)))
                sum1 += temp
                #r += 2

            return sum1    
            '''
     
    else:
    	if a[1] > a[0]/2:
            sum1 = 0
            for j in xrange(a[1] + 2, a[0] + 1, 2):
                sum1 += ncr(a[0], j)
        
            return 2**(a[0] - 1) - sum1
            
        else:    
            sum1 = 0
    	    for j in xrange(1, a[1] + 1, 2):
                sum1 += ncr(a[0], j)
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

modulo = (10**9 + 7)
tt =int(raw_input())
sol = []
for i in xrange(tt):
    a = map(int, raw_input().split())
	
    b = map(int, raw_input().split())
    sol.append(find(a, b))
     
for i in xrange(tt):
    print (sol[i] % modulo) 
