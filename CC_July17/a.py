
def dfs(node, pa, tree, depth, explored):

    stack = []
    stack.append(node)
    stack1 = []
    stack1.append(0)
    pa[node][0] = -1
    while stack:
        u = stack.pop()
        if explored[u] == False:
            explored[u] = True
            depth[u] = stack1.pop()
            for i in tree[u]:
                if explored[i] == False:
                    pa[i][0] = u
                    stack.append(i)    
                    stack1.append(depth[u]+1)
        
def lca(u, v, depth, pa):

    if depth[u] < depth[v]:
        u, v = v, u

    for i in xrange(16, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = pa[u][i]

    if u == v:
        return u

    for i in xrange(16, -1, -1):
        if pa[u][i] != -1 and pa[u][i] != pa[v][i]:
            u = pa[u][i]
            v = pa[v][i]

    return pa[u][0]

def find(u, v, k, depth, pa, tree):

    anc = lca(u, v, depth, pa)
    tot1 = 0
    par = pa[u][0]
    while par != pa[anc][0]:
        temp = tree[u][par]
        if temp <= k:
            tot1 ^= temp
        
        u = par
        par = pa[par][0]
        # print 'last', par, u, temp

    # print 'adsf', tot1
    tot2 = 0
    par = pa[v][0]
    while par != pa[anc][0]:
        temp = tree[v][par]
        if temp <= k:
            tot2 ^= temp
        
        v = par
        par = pa[par][0]
    
    return tot1 ^ tot2 

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    tree = {}
    M = {}
    RM = [-1]*n
    for j in xrange(n-1):
        u, v, c = map(int, raw_input().split())
        M[c] = j
        RM[j] = c
        try:
            t = tree[u]
            tree[u][v] = c
            try:
                t = tree[v]
                tree[v][u] = c
            
            except:
                tree[v] = {u: c}

        except:
            tree[u] = {v: c}
            try:
                t = tree[v]
                tree[v][u] = c

            except:
                tree[v] = {u: c}
    
    depth = [-1]*(n+1)
    explored = [False]*(n+1)
    pa = [[-1]*17 for _ in xrange(n+1)]
    dfs(1, pa, tree, depth, explored)
    for j in xrange(1, n+1):
        for k in xrange(1, 17):
            if pa[j][k-1] != -1:
                pa[j][k] = pa[pa[j][k-1]][k-1]
    
    m = int(raw_input())
    for j in xrange(m):
        u, v, k = map(int, raw_input().split())
        print find(u, v, k, depth, pa, tree)
