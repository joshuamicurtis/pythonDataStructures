def generate_edges(graph):
    """ returns a list of the edges in the graph """
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges
    
def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated
            

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }  

cityGraph = {   'Portland'      :   ['Seattle', 'San Francisco', 'Denver'],
                'Seattle'       :   ['Portland'],
                'San Francisco' :   ['Los Angeles', 'Denver'],
                'Denver'        :   ['San Francisco', 'Los Angeles', 'Portland'],
                'Los Angeles'   :   ['Denver', 'San Francisco']
            }
            
print generate_edges(graph)
print generate_edges(cityGraph)
print find_isolated_nodes(graph)
print find_isolated_nodes(cityGraph)