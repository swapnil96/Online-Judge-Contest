'''Link - https://www.codechef.com/OCT16/problems/SEAARI'''

n, k, d = map(int, raw_input().split())
a = map(int, raw_input().split())
diff = []

for i in xrange(1, n):
	diff.append(a[i] - a[i-1])
	

