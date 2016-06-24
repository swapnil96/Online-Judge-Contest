
try:
    GRAPH = {}
    MAX_PATH = float('-inf')
    visited = set()
    
    det = map(int, raw_input().split())
    no_of_roads = det[1]
 
    if no_of_roads == 1:
        print 2
 
    for _ in xrange(no_of_roads):
        u, v = map(int, raw_input().split())
        GRAPH.setdefault(u, []).append(v)
        GRAPH.setdefault(v, []).append(u)
    
    def LPT(s):
        p1 = 0
        p2 = 0
 
        for v in GRAPH[s]:
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
        return p1
 
 
    start = max(GRAPH.keys())
    visited.add(start)
    x = LPT(start)
    print MAX_PATH + 1

except:
    pass

'''
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

if det[1] >= det[0]:
    print det[0]

else:
    
    try:
        GRAPH = gra
        MAX_PATH = float('-inf')
        visited = set()
    
        def LPT(s):
            p1 = 0
            p2 = 0
 
            for v in GRAPH[s]:
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
            return p1
 
 
        start = max(GRAPH.keys())
        visited.add(start)
        x = LPT(start)
        print MAX_PATH + 1

    except:
        pass



'''