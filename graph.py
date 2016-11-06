class Graph(object):
    """ Demonstrates the essential aspects of a graph """
    def __init__(self, graph_dict=None):
        """ initializes a graph object
            if no dictionary or None is given an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        
    def vertices(self):
        """ returns the vertices of the graph"""
        return list(self.__graph_dict.keys())
        
    def edges(self):
        """ returns the vertices of a graph """
        return self.__generate_edges()
        
    def add_vertex(self, vertex):
        """ if the vertex "vertex" is not in self.__graph_dict, a key "vertex"
            with an empty list as a value is added to the dictionary.
            Otherwise the graph is not changed
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            
    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". 
            Edges are represented as sets with one (a loop back to the 
            vertex), or two vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges
        
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
            
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from a start_vertex to end_vertex in a graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None
        
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths
        
    def vertex_degree(self, vertex):
        """ returns the degree (number of edges connecting to it) of
            the vertex. Loops are counted twice.
        """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree
        
    def min_degree(self):
        """ returns the minimum degree of the vertices """
        min = None
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if min == None:
                min = vertex_degree
            if vertex_degree < min:
                min = vertex_degree
        return min
    
    def max_degree(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max
        
    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)
        
    def density(self):
        """ method to calculate the density of a graph """ 
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V * (V - 1))
        
    def is_connected(self, vertices_encountered=None, start_vertex=None):
        """ determines if a graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict
        vertices = list(gdict.keys()) # "list" necessary in Python3
        if not start_vertex:
            # choose a vertex from graph as starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False
        
    def diameter(self):
        """ calculates the diameter of the graph """
        
        v = self.vertices()
        pairs = [ (v[i], v[j]) for i in range(len(v)-1) for j in range(i+1
                                    , len(v))]
        smallest_paths = []
        for (s,e) in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            #print "Paths:", paths
            #print "Smallest:", smallest
            smallest_paths.append(smallest)
            
        smallest_paths.sort(key=len)
        # longest path is at the end of the list,
        # diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1]) - 1
        return diameter
                
if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print("Add vertex:")
graph.add_vertex("z")

print("Vertices of graph:")
print(graph.vertices())

print("Add an edge:")
graph.add_edge({"a","z"})

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.vertices())
print("Edges of graph:")
print(graph.edges())        

print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)

print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths("a", "b")
print(path)

print('All paths from vertex "a" to vertex "f":')
path = graph.find_all_paths("a", "f")
print(path)

print('All paths from vertex "c" to vertex "c":')
path = graph.find_all_paths("c", "c")
print(path)

print graph.edges()

print 'degrees vertex "a":'
print graph.vertex_degree("a")
print 'degrees vertex "b":'
print graph.vertex_degree("b")
print 'degrees vertex "c":'
print graph.vertex_degree("c")
print 'degrees vertex "d":'
print graph.vertex_degree("d")
print 'degrees vertex "e":'
print graph.vertex_degree("e")
print 'degrees vertex "f":'
print graph.vertex_degree("f")

print 'Minimum degree of graph'
print graph.min_degree()

print 'Max degree of graph'
print graph.max_degree()

print 'Degree sequence'
print graph.degree_sequence()

g = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

complete_graph = { 
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
}

isolated_graph = { 
    "a" : [],
    "b" : [],
    "c" : []
}

graph = Graph(g)
print "density graph"
print(graph.density())

print "density complete graph"
graph = Graph(complete_graph)
print(graph.density())

print "density isolated graph"
graph = Graph(isolated_graph)
print(graph.density())

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
}

g2 = { "a" : ["d","f"],
       "b" : ["c"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

g3 = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}


graph = Graph(g)
print(graph)
print(graph.is_connected())

graph = Graph(g2)
print(graph)
print(graph.is_connected())

graph = Graph(g3)
print(graph)
print(graph.is_connected())


g = { "a" : ["c"],
      "b" : ["c","e","f"],
      "c" : ["a","b","d","e"],
      "d" : ["c"],
      "e" : ["b","c","f"],
      "f" : ["b","e"]
}

graph = Graph(g)
print graph
diameter = graph.diameter()
print "diameter of graph:"
print(diameter)