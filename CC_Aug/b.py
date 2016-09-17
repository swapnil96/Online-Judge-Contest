
#import time
'''
tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = map(int, raw_input().split())
	tot = 0
	fin = set()
	for j in xrange(n):
		if j in fin:
			tot += 1
			continue
			
		nxt = a[j] + j + 1
		if nxt > n - 1:
			nxt = nxt % n

		vis = set()
		while True:
			if nxt == j:
				tot += 1
				fin = vis
				break
	
			nxt = a[nxt] + nxt + 1
			if nxt > n - 1:
				nxt = nxt % n

			if nxt in vis:
				break

			vis.add(nxt)	

	print tot

'''
White = 0
Gray = 1
Black = 2

tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
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
