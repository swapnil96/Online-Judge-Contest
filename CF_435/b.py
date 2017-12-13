
a = {} # 1
b = {} # -1
def dfs(graph, curr, visited, part):

    global a, b

    visited[curr] = 1
    if part == 1:
        a[curr] = 1
    
    else:
        b[curr] = 1

    for i in graph[curr]:
        if visited[i] == -1:
            dfs(graph, i, visited, part*-1) 


n = int(raw_input())
visited = [-1]*(n+1)
graph = {}
for i in xrange(n-1):
    u, v = map(int, raw_input().split())
    if u in graph:
        graph[u][v] = 1

    else:
        graph[u] = {v: 1}

    if v in graph:
        graph[v][u] = 1
    
    else:
        graph[v] = {u: 1}

dfs(graph, 1, visited, 1)
# print a, b, graph
aa = len(a)
bb = len(b)

print aa*bb - (n-1)