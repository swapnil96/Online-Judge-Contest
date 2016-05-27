'''Nicholas and permutation'''
def find(b):

	low = min(b)
	high = max(b)
	lo_idx = b.index(low)
	hi_idx = b.index(high)

	if len(b) == 2:
		return 1 

	if lo_idx < hi_idx:
		got1 = hi_idx
		got2 = len(b) - lo_idx - 1

		return max(got1, got2)

	else:
		got1 = lo_idx
		got2 = len(b) - hi_idx - 1 
		#print got1, got2
		return max(got1, got2)	


t = int(raw_input())
a = raw_input()
b = map(int, a.split())
print (find(b))