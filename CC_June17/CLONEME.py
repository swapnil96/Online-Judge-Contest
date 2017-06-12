# def find(idx, aa, a, b, c, d):

# 	flag = 0
# 	for i in xrange(a-1, b):
# 		for j in dic2[aa[i]]:
# 			if j >= c -1 and j < d and dic2[aa[i]][j] != idx:
# 				dic2[aa[i]][j] = idx
# 				flag += 1
# 				break

# 		if flag == 2:
# 			print "no"
# 			return

# 	print "yes"

def find(aa, a, b, c, d):

	x = aa[a-1:b]
	x.sort()
	y = aa[c-1:d]
	y.sort()
	flag = 0
	for j in xrange(b-a+1):
		if x[j] == y[j]:
			pass

		else:
			flag += 1

		if flag == 2:
			print "NO"
			return

	print "YES"

tt = int(raw_input())
for i in xrange(tt):
	n, q = map(int, raw_input().split())
	aa = map(int, raw_input().split())
	# dic1 = {}
	# dic2 = {}
	# for j in xrange(n):
	# 	try:
	# 		t = dic1[aa[j]]
	# 		dic1[aa[j]][j] = 0

	# 	except:
	# 		dic1[aa[j]] = {j: 0}

	# 	try:
	# 		t = dic2[aa[j]]
	# 		dic2[aa[j]][j] = 0

	# 	except:
	# 		dic2[aa[j]] = {j: 0}

	# print dic1, dic2
	for j in xrange(q):
		a, b, c, d = map(int, raw_input().split())
		find(aa, a, b, c, d)