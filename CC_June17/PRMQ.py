import bisect
 
length = 10**6 + 2
done = [False]*length;
smallest_prime = [0]*length
def Sieve():
 
    smallest_prime[0] = 0
    smallest_prime[1] = 1
    for i in xrange(2, length, 2):
        smallest_prime[i] = 2
 
    for i in xrange(3, length, 2):
    	if done[i] == False:
    		smallest_prime[i] = i
    		for j in xrange(i, length/i+1, 2):
    			if done[i*j] == False:
    				done[i*j] = True
    				smallest_prime[i*j] = i
 
Sieve()
factors = [] 
encr = [[1000000 for _ in xrange(9)] for __ in xrange(10**5+1)]
def factorize(n, a):
    for i in xrange(9):
	encr[0][i] = 0

    for i in xrange(n):
        k = a[i]
        dic = {}
        while k>1:
            try:
                dic[smallest_prime[k]] += 1
 
            except:
                dic[smallest_prime[k]] = 1
 
            k/=smallest_prime[k]
 
        factors.append(dic)
        idx = 1
        encr[i+1][0] = 0
        for j in dic:
        	encr[i+1][idx] = j
        	matrix[i+1][idx] = dic[j]
        	idx += 1
 
matrix = [[0 for _ in xrange(9)] for __ in xrange(10**5+1)]
cur_sum = [[0 for _ in xrange(9)] for __ in xrange(10**5+1)]
def build(main):

	# cur_sum[0][1] = matrix[0][1]
	# for i in xrange(1, 10**5):
	# 	cur_sum[i][1] = cur_sum[i-1][1] + matrix[i][1]

	# for i in xrange(1, 9):
	# 	cur_sum[0][i] = cur_sum[0][i-1] + matrix[0][i]

	for i in xrange(1, n+1):
		for j in xrange(1, 9):
			cur_sum[i][j] = cur_sum[i][j-1] + cur_sum[i-1][j] - cur_sum[i-1][j-1] + matrix[i][j]

n = int(raw_input())
a = map(int, raw_input().split())
q = int(raw_input())

factorize(n, a)
print encr[:6]
build(factors)
print matrix[:6], cur_sum[:6]
for i in xrange(q):
    l, r, x, y = map(int, raw_input().split())
    # idx1 = bisect.bisect_left(encr[l-1], x)
    # idx2 = bisect.bisect_left(encr[r-1], x)
    # idx3 = bisect.bisect_left(encr[l-1], y)
    # idx4 = bisect.bisect_left(encr[r-1], y)
    idx1 = bisect.bisect(encr[l-1], x) - 1
    idx2 = bisect.bisect(encr[r], x) - 1
    idx3 = bisect.bisect(encr[l-1], y) - 1
    idx4 = bisect.bisect(encr[r], y)

    a1 = cur_sum[r][idx4]
    a2 = cur_sum[r][max(0, idx2-1)]
    a3 = cur_sum[l-1][max(0, idx3-1)]
    a4 = cur_sum[l-1][max(0, idx1-1)]    
    print idx1, idx2, idx3, idx4, a1, a2, a3, a4, encr[r]
    print a1 + a2 + a3 - a4
