
def dfs():



n, q = map(int, raw_input().split())
r, key = map(int, raw_input().split())

line = {}
keys = {}
keys[r-1] = key
for i in xrange(n-1):
    u, v, k = map(int, raw_input().split())
    line[u-1] = v
    keys[u-1] = k

query = 0
for i in xrange(q):
    a = map(int, raw_input().split())
    if len(a) == 4:
	    for j in xrange(a):
	    	a[j] = a[j] ^ a[0]    	
    	
    else:
    	for j in xrange(a):
	    	a[j] = a[j] ^ (a[0] ^ 1)    	

    if a[0] == 0:
        line[a[2]] = a[1]
        keys[a[2]] = a[3]

    else:
		
		dfs(a[1])	        
