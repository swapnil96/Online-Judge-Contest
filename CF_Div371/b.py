
n = int(raw_input())
a = map(int, raw_input().split())
count = 1
temp = []
avg = (max(a) + min(a)) / 2.0
temp.append(a[0])
ans = "YES"
got = 0
for i in xrange(n):
	if a[i] in temp:
		pass

	else:	
		temp.append(a[i])
		count += 1

	if count > 3:
		ans = "NO"
		break	

	if a[i] == avg:
		got = 1
		ans = "YES"	

if avg % 1 != 0:
	ans = "NO"

if count <= 2:
	ans = "YES"
	
if count > 2 and got == 0:
	ans = "NO"

print ans

