
n = int(raw_input())
a = map(int, raw_input().split())

temp = []
for i in xrange(n-1):
	temp.append(a[i] + a[i+1])

temp.append(a[n-1])
print ' '.join(map(str, temp))

