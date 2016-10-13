graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(graph, start, end, length, path=[]):
    
    path = path + [start]
    length += 1
    if start == end:
        return ([path], length)
    
    if not graph.has_key(start):
        return ([],0)
    
    paths = []
    lengths = []
    for node in graph[start]:
        if node not in path:
    
            newpaths = find_path(graph, node, end, length, path)
    
    	    for newpath in newpaths:
    	       	paths.append(newpath)
                lengths.append(length)

    return (paths, lengths)        

print find_path(graph, 'A', 'D', 0)    