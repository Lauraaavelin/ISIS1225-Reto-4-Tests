from DataStructures.Graph import adj_list_graph as g
from DataStructures.Map import map_linear_probin as map
from DataStructures.List import array_list as lt
from DataStructures.List import colas as cola
from DataStructures.List import pilas as stack
from DataStructures.Graph import graph_search as gs


def breath_first_search(graph, source):
    """
    Genera un recorrido BFS sobre el grafo graph
    Args:
        graph:  El grafo a recorrer
        source: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    
    search = gs.new_graph_search(source)
    search['visited'] = map.new_map(num_elements=g.num_vertices(graph),load_factor=0.75)
    map.put(search['visited'], source, {'marked': True,
                                        'edge_to': None,
                                        'dist_to': 0
                                        })
    bfs_vertex(search, graph, source)
    return search
    


def bfs_vertex(search, graph, source):
    """
    Funcion auxiliar para calcular un recorrido BFS
    Args:
        search: Estructura para almacenar el recorrido
        vertex: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    adjsqueue = cola.new_queue()
    cola.enqueue(adjsqueue, source)
    while not (cola.is_empty(adjsqueue)):
        vertex = cola.dequeue(adjsqueue)
        visited_v = map.get(search['visited'], vertex)
        adjslst = g.adjacents(graph, vertex)
        for w in lt.iterator(adjslst):
            visited_w = map.get(search['visited'], w["vertex_b"])
            if visited_w is None:
                dist_to_w = visited_v['dist_to'] + 1
                visited_w = {'marked': True,
                                'edge_to': vertex,
                                "dist_to": dist_to_w
                                }
                map.put(search['visited'], w["vertex_b"], visited_w)
                cola.enqueue(adjsqueue, w["vertex_b"])
    return search
    


def has_path_to(search, vertex):
    """
    Indica si existe un camino entre el vertice source
    y el vertice vertex
    Args:
        search: Estructura de recorrido BFS
        vertex: Vertice destino
    Returns:
        True si existe un camino entre source y vertex
    Raises:
        Exception
    """
   
    element = map.get(search['visited'], vertex)
    if element and element['marked'] is True:
        return True
    return False
    


def path_to(search, vertex):
    """
    Retorna el camino entre el vertices source y el
    vertice vertex
    Args:
        search: La estructura con el recorrido
        vertex: Vertice de destingo
    Returns:
        Una pila con el camino entre el vertices source y el
        vertice vertex
    Raises:
        Exception
    """

    if has_path_to(search, vertex) is False:
        return None
    path = stack.new_pila()
    while vertex != search['source']:
        stack.push(path, vertex)
        vertex = map.get(search['visited'],
                            vertex)['edge_to']
    stack.push(path, search['source'])
    return path
    
