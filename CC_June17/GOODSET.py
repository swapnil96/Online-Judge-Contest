ans = [1]
for i in xrange(2, 501):

	length = len(ans)
	flag = 0
	for j in xrange(length):
		if ans[j] == i:
			flag = 1
			break

		for k in xrange(j+1, length):
			if ans[k] + ans[j] == i:
				flag = 1
				break

	if flag == 0: 
		ans.append(i)

# print ans, len(ans)
tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	print ' '.join(map(str, ans[:n]))	