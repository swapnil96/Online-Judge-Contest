

def amazingness(a):
    
    s = []
    ans = 0;
    
    for i in xrange(0, len(a)):
        
        val = 0;
        
        m = a[i] % 4
        
        if m == 0: 
        	got = a[i]

		if m = 1:
			got = 1
	
		if m = 2:
			got = a[i] + 1
		
		if m = 3:
			got = 0

        for j in xrange(i, len(a)):
            
            val ^= a[j];  
            
            if val in s :
               pass

            else:	
                
            	ans += val;
                s.append(val)           

    return ans

def find(que):

	ans = 0
	if que[0] > que[1]:
		
		for i in xrange(que[1], que[0]+1):

			p = map(int, str(i))
			ans += amazingness(p)
		
	else:	
		
		for i in xrange(que[0], que[1]+1):

			p = map(int, str(i))
			ans += amazingness(p)
		
	return  ans	% (10^9 + 7)

tt = int(raw_input())
sol = []

for i in xrange(tt):

	a = raw_input()
	b = map(int, a.split())

	sol.append(find(b))

for i in xrange(0, tt):

	print sol[i]	
   	

