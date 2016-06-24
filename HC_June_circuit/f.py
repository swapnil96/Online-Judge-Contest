
import sys

k = int(raw_input())
a = map(int, (' '.join(n for n in raw_input())).split())
b = map(int, (' '.join(l for l in raw_input())).split())
length = len(a)
temp = []
for i in xrange(length):
	if a[i] > b[i]:
		temp.append(9 - a[i] + b[i])

	temp.append(b[i] - a[i])

if a == b:
	print 0
	sys.exit()

if k == 1:
	c = temp.count(0)
	print length - c
	sys.exit()

if k == 0:
	print -1
	sys.exit()

ans = 0
while sum(temp) != 0:
	for i in xrange(length):
		if temp[i] == 0:
			continue
		got = 0

		for j in xrange(i, i + k):
			if j > length - 1:
				break

			if temp[j] == 0:
				got = 1
				break

		print temp, i, j		
		if j - i == 1 and got == 1:
			ans += 1
			temp[i] = 0
			continue

		cut = min(temp[i:j + 1])		
		new = [l - cut for l in temp[i:j + 1]]
		temp = temp[:i] + new + temp[j+1:]			
		ans += 1
		print temp

print ans	