def matrixRegionSum2(matrix, A, D, sums):
	if len(matrix)==0:
		return
	
	if A[0]==0 or A[1]==0: 
		OA=0 

	else: 
		OA=sums[A[0]-1][A[1]-1]   

	if A[1]==0: 
		OC=0 

	else:
		OC=sums[D[0]][A[1]-1]   

	if A[0]==0: 
		OB=0 

	else: 
		OB=sums[A[0]-1][D[1]]   

	OD=sums[D[0]][D[1]]   

	return OD-OB-OC+OA

from numpy import *

tt = map(int, raw_input().split())
temp = []
for i in xrange(tt[0]):
	temp.append(map(int, raw_input().split()))

que = array(temp)
sums = que.cumsum(axis = 0).cumsum(axis = 1)
print sums
print matrixRegionSum2(que, [1,2], [2,3], sums)