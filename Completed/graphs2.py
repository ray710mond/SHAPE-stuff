g = \
{'A': ['B','C'],
 'B': ['A','D','C'],
 'C': ['A','B','D','E'], 
 'D': ['B','C','E','F'],
 'E': ['C','D','F'],
 'F': ['D','E']}

def topo_sort(graph):

    indegrees = {}
    for s in graph:
        indegrees[s] = 0
    for s in graph:
        for t in graph[s]:
            indegrees[t] += 1
    
    output = []
    q = []
    for s in indegrees:
        if indegrees[s] == 0:
            q.append(s)

    while q:
        s = q.pop(0)
        output.append(s)
        for t in graph[s]:
            indegrees[t] -= 1
            if indegrees[t] == 0:
                q.append(t)
    return output

def bfs(graph, source):
    q = []
    discovered = set()
    output = []
    found = False
    q.append(source)
    discovered.add(source)

    while not found and q: 
        v = q.pop(0)
        output.append(v)
        for neighbor in graph[v]:
            if neighbor not in discovered: 
                discovered.add(neighbor)
                q.append(neighbor)
    return output

def dfs(graph, source):
    stack = []
    discovered = set()
    output = []
    found = False
    stack.append(source)
    discovered.add(source)

    while not found and stack: 
        v = stack.pop()
        output.append(v)
        for neighbor in graph[v]:
            if neighbor not in discovered: 
                discovered.add(neighbor)
                stack.append(neighbor)
    return output

print(bfs(g, 'A'))
print(dfs(g, 'A'))

def unweighted_shortest_path1(graph, source):
    q = []
    discovered = set()
    costDict = {'A': 0}
    found = False
    q.append(source)
    discovered.add(source)

    while not found and q: 
        v = q.pop(0)
        for neighbor in graph[v]:  
            if neighbor not in discovered: 
                discovered.add(neighbor)
                q.append(neighbor)
                costDict[neighbor] = costDict[v] + 1
    return costDict

print(unweighted_shortest_path1(g, 'A'))

def unweighted_shortest_path2(graph, source, target):
    q = []
    discovered = set()
    pathDict = {'A': None}
    found = False
    q.append(source)
    discovered.add(source)

    while not found and q: 
        v = q.pop(0)
        for neighbor in graph[v]:  
            if neighbor not in discovered: 
                discovered.add(neighbor)
                q.append(neighbor)
                pathDict[neighbor] = v
    path = []
    i = target
    path.append(target)
    while(pathDict[i] != None):
        path.append(pathDict[i])
        i = pathDict[i]
    print(path)
    return pathDict
print(unweighted_shortest_path2(g, 'A', 'F'))