def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen or (t == 8 and len(path) != 2):
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen, t_path))
    return paths
     

def LPT(s):
    p1 = 0
    p2 = 0
    for v in gra[s]:
        if v in visited:
            continue
 
        visited.add(v) 
        value = LPT(v) + 1
        if value > p1:
            p1 = value
            continue
        elif value == p1 or value > p2:
            p2 = value
            continue
 
    global MAX_PATH
    MAX_PATH = max(MAX_PATH, p1 + p2)
    print MAX_PATH, p1, p2, visited, s
    return p1 + 1

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]

  return path    

  
def cycle_exists(G):                      # - G is an undirected graph.              
    marked = { u : False for u in G }     # - All nodes are initially unmarked.
    found_cycle = [False]                 # - Define found_cycle as a list so we can change
                                          # its value per reference, see:
                                          # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment
 
    for u in G:                           # - Visit all nodes.
        if not marked[u]:
            dfs_visit(G, u, found_cycle, u, marked)     # - u is its own predecessor initially
        if found_cycle[0]:
            break
    return found_cycle[0]
 
#--------
 
def dfs_visit(G, u, found_cycle, pred_node, marked):
    if found_cycle[0]:                                # - Stop dfs if cycle is found.
        return
    marked[u] = True                                  # - Mark node.
    for v in G[u]:                                    # - Check neighbors, where G[u] is the adjacency list of u.
        if marked[v] and v != pred_node:              # - If neighbor is marked and not predecessor,
            found_cycle[0] = True                     # then a cycle exists.
            return
        if not marked[v]:                             # - Call dfs_visit recursively.
            dfs_visit(G, v, found_cycle, u, marked)


  

det = map(int, raw_input().split())
gra = {}
#vertex = []
for i in xrange(det[1]):
    a = map(int, raw_input().split())
    #if a[0] not in vertex:
    #    vertex.append(a[0])

    #if a[1] not in vertex:
    #    vertex.append(a[1])

    if a[0] not in gra:
        gra[a[0]] = []

    if a[1] not in gra:
        gra[a[1]] = []

    gra[a[0]].append(a[1])
    gra[a[1]].append(a[0])

'''
high = -1
for i in xrange(det[0]):   
    all_paths = DFS(gra, i+1) 
    max_path  = max(all_paths, key=lambda l: len(l))
    this = len(max_path)
    if this > high:
        high = this
'''

'''
all_paths = DFS(gra, a[0]) 
max_path  = max(all_paths, key=lambda l: len(l))
length = len(max_path)
start = max_path[length - 1]
all_paths = DFS(gra, start)
max_path  = max(all_paths, key=lambda l: len(l))
print len(max_path)
'''
'''
print gra
visited = set()
MAX_PATH = float('-inf')
start = max(gra.keys())
visited.add(start)
x = LPT(start)
print MAX_PATH , x
'''
'''
road = iterative_bfs(gra, 1)
s = road[len(road) - 1]
fin = iterative_bfs(gra, s)
print len(fin)
'''
print cycle_exists(gra)
print DFS(gra, 8)