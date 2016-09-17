
def allOnes(n):
    return ((n+1) & n == 0) and (n!=0)

n = int(raw_input())
a = map(int, raw_input().split())
tot = 0
for i in xrange(n):
	till = a[i]
	for j in xrange(i+1, n):
		till = max(till, a[j])
		if (a[i] & a[j] == a[j]) or (a[i] & a[j] == a[i]):
			tot += till
			#print till, a[i], a[j]

print tot	