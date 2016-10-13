
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

n = int(raw_input())
a = map(int, raw_input().split())
temp = []
for i in xrange(n):
	temp.append(raw_input())


for i in xrange(n):
		
	count = 0	
	for j in xrange(len(temp[i])):

		if temp[i][j] in vowels:
			count += 1

	if count == a[i]:
		ans = 'YES'

	else:
		ans = "NO"
		break

print ans					

