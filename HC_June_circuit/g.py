
'''
import itertools

a = map(int, raw_input().split())
cost = []
nut = []
MOD = 10**9 + 7
for i in xrange(a[0]):
	b = map(int, raw_input().split())
	cost.append(b[0])
	nut.append(int(str(b[1]), 2))

num = [1 for i in xrange(a[1])]
bit = int(''.join(map(str, num)), 2)
ans = {}
stuff = range(0, a[0])
for L in range(0, a[0]+1):
	for subset in itertools.combinations(stuff, L):
		if bool(subset):
			pro = 1
			andbit = bit
			for i in subset:
				pro *= (cost[i] % MOD)
				andbit = andbit & nut[i]
			
			y = bin(andbit).count('1')
			if y not in ans:
				ans[y] = []
			
			ans[y].append(pro)


#print ans, len(ans)
fin = []
for i in xrange(a[1] + 1):
	if i in ans:
		fin.append(sum(ans[i]) % MOD)

	else:
		fin.append(0)	

print ' '.join(map(str, fin))	
'''	

from itertools import izip, chain
import itertools

a = map(int, raw_input().split())
que = {}
MOD = 10**9 + 7
for i in xrange(a[0]):
	b = map(str, raw_input().split())
	e = int(b[0])
	f = int(b[1], 2)
	if f not in que:
		que[f] = []

	que[f].append(e)

print que
bit = pow(2, a[1]) - 1
for L in que.values():  
	x = [1]  
	for i in L:
    		x = [c + b*i for c,b in izip(chain([0],x), chain(x,[0]))]
	
	tot = sum(x) - 1
	que[que.keys()[que.values().index(L)]] = tot

ans = {}
g = len(que)
stuff = range(0, g)
cost = que.values()
nut = que.keys()
print que, cost, nut
for L in range(0, g + 1):
	for subset in itertools.combinations(stuff, L):
		if bool(subset):
			pro = 1
			andbit = bit
			for i in subset:
				pro *= (cost[i] % MOD)
				andbit = andbit & nut[i]
			
			y = bin(andbit).count('1')
			if y not in ans:
				ans[y] = []
			
			ans[y].append(pro)
			print subset

fin = []
#print ans, a[0]
for i in xrange(a[1] + 1):
	if i in ans:
		fin.append(sum(ans[i]) % MOD)

	else:
		fin.append(0)	
print ' '.join(map(str, fin))

