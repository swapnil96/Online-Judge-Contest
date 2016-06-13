import math
#def factors(n):    
 #   return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def factors(n):
    
    if n % 2 == 0:
    	step = 1

    else:
    	step = 2	   
    #step = 2 if n%2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))

def corr(idx, chg, las):

	#print idx, chg, las
	
	divi = list(factors(idx))
	for q in divi:
		pre[q-1] = (pre[q-1] / las) * chg
	'''
	for i in xrange(1, idx+1):
		if idx % i == 0:
			pre[i-1] = (pre[i-1] / las) * chg
	'''		
	#print pre		

def find(no):

    sum1 = sum(que1[0::no])
    pro = pre[no - 1]
    inte = int(sum1)   
    fra = sum1 - inte
    got = round(10**(fra+5), 2)
    return ((str(got)[0]), pro)    

n = int(raw_input())
que = map(int, raw_input().split())
que1 = [0.0]*n
query = int(raw_input())
MOD = 10**9 + 7
for q in xrange(n):
    que1[q] = math.log10(que[q])

pre = []
for i in xrange(1, n+1):
	pro = 1
	for j in xrange(0, n, i):
		pro = ((pro)*que[j]) % MOD

	pre.append(pro)
	#print pre

sol = []
k = 0
for v in xrange(query):
    a = map(int, raw_input().split())
    if a[0] == 1:
        que1[a[1] - 1] = math.log10(a[2])
        las = que[a[1] - 1]
        que[a[1] - 1] = a[2]
        corr(a[1] - 1, a[2], las)

    else:
        k += 1
        sol.append(find(a[1]))

for v in xrange(k):
	print ' '.join(map(str, sol[v]))

