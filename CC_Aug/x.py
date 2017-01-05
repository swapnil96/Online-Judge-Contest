n = input()
adj_matrix = [[int(s) for s in raw_input().split()] for _ in xrange(n)]
adj_list = {i: [] for i in xrange(n)}
for i in xrange(n):
    for j in xrange(n):
        if adj_matrix[i][j]:
            adj_list[i].append(j)
m = input()
for _ in xrange(m):
    k, x = [int(s) for s in raw_input().split()]
    nodes = frozenset([x-1])
    level = 0
    seen = {}
    while nodes and level < k:
        nodes = frozenset(nn for n in nodes for nn in adj_list[n])
        if nodes in seen:
            cycle_len = level - seen[nodes]
            level += ((k-level-1)/cycle_len)*cycle_len+1
        else:
            seen[nodes] = level
            level += 1
    print len(nodes)
    if nodes:
        print ' '.join(str(n+1) for n in sorted(nodes))
    else:
        print -1 
