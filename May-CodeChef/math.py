import itertools

def fib(inpnum, lo):
	
	fiblist=[]
	a, b = 1, 2
	

	while a <= inpnum:

		fiblist.append(a)
		a, b = b, a+b
	
	add = []
	for subset in itertools.combinations(fiblist, lo):
   		
   		temp = 0
   		
   		for j in xrange(0, lo):
   			temp += subset[j]
   			
   		add.append(temp)
   		print add, subset 

   	ans = add.count(inpnum)
   	return ans	

tt = int(raw_input())
sol = []
for i in xrange(tt):

	a = raw_input()
	b = map(int, a.split())
	sol.append(fib(b[0], b[1]))

for i in xrange(0, tt):

	print sol[i]	

