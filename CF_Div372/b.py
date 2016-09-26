

'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

t = raw_input()
got = 0
length = len(t)
start = 0
for i in xrange(length):

	if i+25 > length-1:
		break

	dic = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
	ans = ''
	where = []
	ix = 0
	for j in xrange(i, i+26):
		if t[j] == "?":
			where.append(ix)
			ans += "?"
			if j == i+25:
				start = i
				got = 1
				break

		else:	
			dic[t[j]] += 1
			if dic[t[j]] > 1:
				break	

			ans += t[j]	
			if j == i+25:
				start = i
				got = 1
				break	

		ix += 1

	if 	got == 1:
		break

idx = 0
if got == 1:
	#print dic, ans
	for j in dic:
		if dic[j] == 0:
			#print ans, where[idx]
			#qwe = ''
			ans = ans[:where[idx]] + j + ans[where[idx]+1:]
			#print ans, 'asdf'
			idx += 1
	
	fin = t[:start] + ans + t[start+26:]	
	for k in xrange(length):
		if fin[k] == "?":
			fin = fin[:k] + "A" + fin[k+1:]	

	#print ans
	print fin#, where[0]

else:
	print -1