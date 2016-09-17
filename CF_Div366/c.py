
n, q = map(int, raw_input().split())
query = []
for i in xrange(q):
	query.append(map(int, raw_input().split()))

noti = [0]*n
uread = [0]*n
tot = 0
seq = []
last = 0
tempo = [0]*n
for i in xrange(q):
	if query[i][0] == 1:
		noti[query[i][1] - 1] += 1
		uread[query[i][1] - 1] += 1
		seq.append(query[i][1] - 1)
		tot += 1

	elif query[i][0] == 2:
		tot -= uread[query[i][1] - 1]
		uread[query[i][1] - 1] = 0

	else:
		if query[i][1] > last:
			for j in xrange(last, query[i][1]):
				temp = seq[j]
				tempo[temp] += 1
				if (noti[temp] - uread[temp]) >= tempo[temp]:
					pass

				else:	
					uread[temp] -= 1
					tot -= 1

			last = query[i][1]
			
	print tot			
