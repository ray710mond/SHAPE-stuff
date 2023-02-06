class Vertex:

    def __init__(self, name, adjacent = []):
        self.name = name
        self.adjacent = adjacent


class Edge:
    def __init__(self, src, target, weight = 1):
        self.src = src
        self.target = target
        self.weight = weight

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        new_vertex = Vertex(name)
        self.vertices[name] = new_vertex
    
    def add_edge(self, src, target):
        new_edge = Edge(src, target)
        
        

b = Vertex("B")
a = Vertex("A")
