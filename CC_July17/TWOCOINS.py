
def dfs(tree, n):

    explored = [False]*(n+1)
    stack = [1]
    count = 0
    pa = [-1]*(n+1)
    while stack:
        u = stack.pop()
        if explored[u] == False:
            explored[u] = True
            curr = pa[u]
            if len(tree[u]) == 1 or u == 1 or curr == -1: 
                count += 1

            for i in tree[u]:
                if explored[i] == False:
                    stack.append(i)    
                    pa[i] = -1*curr

        # print stack, pa

    print count

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    # tree = {}
    # for j in xrange(n-1):
    #     u, v = map(int, raw_input().split())
    #     try:
    #         t = tree[u]
    #         tree[u][v] = 0
    #         try:
    #             t = tree[v]
    #             tree[v][u] = 0
            
    #         except:
    #             tree[v] = {u: 0}

    #     except:
    #         tree[u] = {v: 0}
    #         try:
    #             t = tree[v]
    #             tree[v][u] = 0

    #         except:
    #             tree[v] = {u: 0}

    tree = [[] for _ in xrange(n+1)]
    for j in xrange(n-1):
        u, v = map(int, raw_input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    dfs(tree, n)