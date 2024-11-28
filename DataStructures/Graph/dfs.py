from DataStructures.Graph import adj_list_graph as g
from DataStructures.Map import map_linear_probin as map
from DataStructures.List import array_list as lt
from DataStructures.List import pilas as pila
from DataStructures.Graph import graph_search as gs

def depth_first_search(my_graph, source):
    search = gs.new_graph_search(source)

    search['visited'] = map.new_map(num_elements=g.num_vertices(my_graph),load_factor=0.75) #se crea el mapa de los que ya fueron visitados y de donde vienen 

    map.put(search['visited'], source, ({'marked': True, 'edge_to': None}))
    dfs_vertex(search, my_graph, source)
    return search

def dfs_vertex(search, graph,vertex):
    adjlst = g.adjacents(graph, vertex)
    for w in lt.iterator(adjlst):
        visited = map.get(search['visited'], w["vertex_b"])
        if visited is None: #si el nodo no esta visitado marquelo sino contunue
            map.put(search['visited'],w["vertex_b"], {'marked': True, 'edge_to': vertex})
            dfs_vertex(search, graph, w["vertex_b"])
    return search

def has_path_to(search, vertex):
    element = map.get(search['visited'], vertex) # devuelve el diccionario de si ya esta visitado o no 
    
    if element and element['marked'] is True: # revisa si esta marcado, si lo esta significa que hay un camino 
        return True
    return False

def path_to(search, vertex):
    if has_path_to(search, vertex) is False:
        return None
    path = pila.new_pila()
    while vertex != search['source']:
        pila.push(path, vertex)
        vertex = map.get(search['visited'], vertex)['edge_to']
    pila.push(path, search['source'])
    return path