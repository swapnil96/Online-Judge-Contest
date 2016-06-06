
import string
import math

def find1(a):

	no = int(math.sqrt(2*a))
	ans = ''.join(map(str, (['a' for j in xrange(no - 1)])))
	#print len(ans)
	need = a - (no*(no - 1))/2
	if need < 26:
		ans += string.ascii_lowercase[1:need+1]
	
	else:
		#print need
		no1 = int(math.sqrt(2*need))
		ans1 = ''.join(map(str, (['b' for j in xrange(no1 - 1)])))
		final = need - (no1*(no1 - 1))/2
		ans += ans1
		ans += string.ascii_lowercase[2:final+2]	

	return ans

eve = string.ascii_lowercase

def find(a):

	quo = a / 26
	rem = a % 26
	ans = ''
	for i in xrange(quo):
		ans += eve

	ans += eve[:rem]
	return ans	

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = int(raw_input())
	#if a <= 26:
	#	sol.append(string.ascii_lowercase[0:a])

	#else:
	#	sol.append(find(a))	
	sol.append(find(a))

for i in xrange(tt):
	print sol[i]		