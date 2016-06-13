

a = map(int, raw_input().split())
b = map(int, raw_input().split())
temp1 = b[:(a[1] - 1)]
temp2 = b[a[1]:]
len1 = len(temp1)
len2 = len(temp2)
#print temp1, temp2, len1
if b[a[1] - 1] == 0:
	count = 0 

else:
	count = 1

if len1 > len2:
	temp1.reverse()
	#print temp2
	for i in xrange(len2):
		if temp2[i] == 1 and temp1[i] == 1:
			count += 2

	for i in xrange(len2, len1):
		if temp1[i] == 1:
			count += 1		

elif len1 < len2:
	temp1.reverse()
	for i in xrange(len1):
		if temp2[i] == 1 and temp1[i] == 1:
			count += 2

	for i in xrange(len1, len2):
		if temp2[i] == 1:
			count += 1		

else:
	temp1.reverse()
	for i in xrange(len1):
		if temp1[i] == 1 and temp2[i] == 1:
			count += 2

print count
