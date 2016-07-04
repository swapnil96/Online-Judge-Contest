
def find(a, n):
	
	avg = (sum(a) + 0.0)/n
	if (max(a) == 5) and (min(a) > 2) and (avg >= 4) :
		return 'Yes'

	return 'No'	

tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = map(int, raw_input().split())
	print find(a, n)