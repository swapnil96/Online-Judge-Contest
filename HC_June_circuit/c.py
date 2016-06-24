
import sys

det = map(int, raw_input().split())
gra = {}
for i in xrange(det[1]):
	a = map(int, raw_input().split())
	if a[0] not in gra:
		gra[a[0]] = {a[1]: a[2]}

	if a[1] not in gra:
		gra[a[1]] = {a[0]: a[2]}

	gra[a[0]][a[1]] = a[2]
	gra[a[1]][a[0]] = a[2]

dist = {}
for i in gra:
	dist[i] = sum(gra[i].values())

vertex = []
for i in xrange(det[2]):
	fin = max(dist.values())
	if fin <= 0:
		break

	idx = dist.keys()[dist.values().index(fin)]
	vertex.append(idx)	
	dist.pop(idx)	
	for j in gra[idx]:
		if j not in dist:
			continue
		dist[j] -= gra[idx][j]

print len(vertex)
for i in xrange(len(vertex)):
	print vertex[i]

sys.exit()	