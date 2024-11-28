from DataStructures.Graph import edge as ed
from DataStructures.Map import map_linear_probin as th
from DataStructures.List import array_list as lt


def new_graph(size=15, directed=False):
    graph = {
        "directed": directed,
        "size": size,
        "vertices": th.new_map(size, 0.5),
        "edges": 0,
        "in_degree": None,
        "information": th.new_map(size, 0.5),
        "type": "ADJ_LIST",
    }
    if directed:
        graph['in_degree'] = th.new_map(size, 0.5)
    return graph

def insert_vertex(graph, key_vertex, info_vertex):
    if th.get(graph["information"],key_vertex) == None:
       th.put( graph["information"], key_vertex, info_vertex)
       lista=lt.new_list()
       th.put(graph["vertices"],key_vertex,lista)
       if (graph['directed']):
            th.put(graph['in_degree'], key_vertex, 0)
    return graph



def remove_vertex(my_graph, key_vertex):

    if not th.contains(my_graph['vertices'], key_vertex):
        return my_graph

  
    adj_list = th.get(my_graph['vertices'], key_vertex)

    for edge in adj_list['elements']:
        vertex_b = edge['vertex_b']
        adj_list_b = th.get(my_graph['vertices'], vertex_b)
        adj_list_b['elements'] = [e for e in adj_list_b['elements'] if e['vertex_b'] != key_vertex]
        my_graph['edges'] -= 1

    
        if my_graph['directed']:
            in_degree = th.get(my_graph['in_degree'], vertex_b)
            if in_degree is not None:
                th.put(my_graph['in_degree'], vertex_b, in_degree - 1)

    
    th.remove(my_graph['vertices'], key_vertex)
    if my_graph['directed'] and my_graph['in_degree'] is not None:
        th.remove(my_graph['in_degree'], key_vertex)

    return my_graph    

def num_vertices(graph):
    return graph["vertices"]["size"]

def num_edges(graph):
    return graph["edges"]

def edge_exists(lst, vertex_a, vertex_b):
    """ Verifica si una arista entre dos vértices ya existe en la lista. """
    for edge in lt.iterator(lst):
        if (edge['vertex_a'] == vertex_a and edge['vertex_b'] == vertex_b) or \
           (edge['vertex_a'] == vertex_b and edge['vertex_b'] == vertex_a):
            return True
    return False

def edges(graph):
    lstmap = graph['vertices']
    lstresp = lt.new_list()

    for bucket in lstmap['table']['elements']:
        if bucket is not None:
            key, adj_list = bucket  
            for edge in adj_list['elements']:
                if graph['directed']:
                    lt.add_last(lstresp, edge)
                elif not edge_exists(lstresp, edge['vertex_a'], edge['vertex_b']):
                    lt.add_last(lstresp, edge)
    return lstresp


def degree(graph, key_vertex):
    if graph["edges"]== 0:
        return None
    lista=th.get(graph["vertices"],key_vertex)
    if lista:
        return lista["size"]
    else:
        return None

def out_degree(graph, vertex):
    return int(len(graph["info"].get(vertex, [])))


def contains_vertex(my_graph, key_vertex):
    return th.contains(my_graph['vertices'], key_vertex)


def adjacent_edges(my_graph, vertex):
    
    if not th.contains(my_graph['vertices'], vertex):
        return lt.new_list()  

    adj_list = th.get(my_graph['vertices'], vertex)
    adj_edges = lt.new_list()

    for edge in adj_list['elements']:
        lt.add_last(adj_edges, edge)

    return adj_edges


def add_edge(my_graph, vertex_a, vertex_b, weight=0):

    if not th.contains(my_graph['vertices'], vertex_a) or not th.contains(my_graph['vertices'], vertex_b):
        return my_graph

    adj_list_a = th.get(my_graph['vertices'], vertex_a)
    adj_list_b = th.get(my_graph['vertices'], vertex_b)


    arco_actualizado = False
    for edge in adj_list_a['elements']:
        if edge['vertex_a'] == vertex_a and edge['vertex_b'] == vertex_b:
            edge['weight'] = weight
            arco_actualizado = True
            break

    if not arco_actualizado:
        # Agregar el arco vertex_a -> vertex_b a la lista de adyacencia de vertex_a
        new_edge = ed.new_edge(vertex_a, vertex_b, weight)
        lt.add_last(adj_list_a, new_edge)
        my_graph['edges'] += 1

        # Si el grafo es no dirigido, agregar el arco vertex_b -> vertex_a a la lista de adyacencia de vertex_b
        if not my_graph['directed']:
            new_edge = ed.new_edge(vertex_b, vertex_a, weight)
            lt.add_last(adj_list_b, new_edge)
        else:
            # Si el grafo es dirigido, incrementar el grado de entrada del vertice_b
            if my_graph['in_degree'] is None:
                my_graph['in_degree'] = th.new_map(my_graph['size'], 0.5)
            in_degree = th.get(my_graph['in_degree'], vertex_b)
            if in_degree is None:
                in_degree = 0
            th.put(my_graph['in_degree'], vertex_b, in_degree + 1)

    return my_graph


def vertices(graph):
    return th.key_set(graph["vertices"])

def in_degree(graph, key_vertex):
    if graph["directed"]:
        return th.get(graph["in_degree"],key_vertex)
    else:
        x= th.get(graph["vertices"],key_vertex)
        if x:
            
            return x["size"]
        else:
            return None 
        
    
def get_edge(graph, vertex_a, vertex_b):
    #el arco que vaya del vertice A al vertice B, sea dirigido o no que venga de la lista de b
    lista_de_arcos=th.get(graph["vertices"],vertex_a)
    for arco in lista_de_arcos["elemnts"]:
        if arco["vertex_b"]==vertex_b:
            return arco
    if lista_de_arcos==None:
        return None 
    
    
def adjacents(graph, key_vertex):
    lista=th.get(graph["vertices"],key_vertex)
    if lista==None:
        return lt.new_list()
    else:
        return lista