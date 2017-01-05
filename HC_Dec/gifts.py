White = 0
Gray = 1
Black = 2

n,m = map(int, raw_input().split())
for i in xrange(m):
	a = map(int, raw_input().split())
	pred = [-1]*n
	vis = [0]*n
	tot = 0
	for j in xrange(n):
		if vis[j] == White:
			vis[j] = Gray
			nxt = a[j] + j + 1
			if nxt > n - 1:
				nxt -= n

			if nxt == j:
				tot += 1
				vis[j] = Black
				continue

			pred[nxt] = j
			while True:
				if vis[nxt] == Black:
					break

				elif vis[nxt] == Gray:
					prev = pred[nxt]
					vis[prev] = Black
					while (pred[nxt] != -1):
						prev = pred[prev]
						vis[prev] = Black
						tot += 1
						if prev == nxt:
							tot += 1
							break

				else:
					vis[nxt] = Gray
					last = nxt
					nxt = a[nxt] + nxt + 1
					if nxt > n - 1:
						nxt -= n

					pred[nxt] = last
					#print pred, vis

	print tot
