from numpy import *
import temp
import time
'''
tt = map(int, raw_input().split())
temp1 = []
for i in xrange(tt[0]):
	temp1.append(map(int, raw_input().split()))

que = array(temp1)
'''
que = array(temp.aol)
tt = [1000, 1000]

sums = que.cumsum(axis = 0).cumsum(axis = 1)
print sums
def matrixRegionSum2(A, D):
	#if len(que) == 0:
	#	return
	
	if A[0] == 0 or A[1] == 0: 
		OA = 0 

	else: 
		OA = sums[A[0]-1][A[1]-1]   

	if A[1] == 0: 
		OC = 0 

	else:
		OC = sums[D[0]][A[1]-1]   

	if A[0] == 0: 
		OB = 0 

	else: 
		OB = sums[A[0]-1][D[1]]   

	OD = sums[D[0]][D[1]]   

	return OD-OB-OC+OA

def find(a):

	ans = 10**9
	total = 0
	total1 = 0
	now = time.time()
	for i in xrange(tt[0]):

		for j in xrange(tt[1]):

			if i + a[0] > tt[0]:
				break

			if j + a[1] > tt[1]:
				break	

			#hul = que[i:i + a[0], j:j + a[1]]
			#then = time.time()
			sum1 = matrixRegionSum2([i, j], [i + a[0] - 1, j + a[1] - 1])
			#total1 += time.time() - then
			#now = time.time() 

			#sum1 = hul.sum()
			#got = a[0]*a[1]*(hul.max()) - sum1
			#hul.max()
			#total += (time.time() - now)
			#print hul, sum1, got
			got = 1
			if got == 0:
				return 0
			if got < ans:
				ans = got

	#print total1, total			
	print time.time()  -now
	return ans			

tc = int(raw_input())
sol = []
got = time.time()
for i in xrange(tc):
	#a = map(int, raw_input().split())	
	a = temp.query[i]
	sol.append(find(a))

for i in xrange(tc):
	print sol[i]	

print time.time() - got	