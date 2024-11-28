from DataStructures.Graph import adj_list_graph as g
from DataStructures.Map import map_linear_probin as map
from DataStructures.List import array_list as lt
from DataStructures.List import colas as cola
from DataStructures.List import pilas as stack
from DataStructures.Graph import dfo_search as dfo_search


def depth_first_order(graph):
    """Iniciar un recorrido Depth FirstOrder(**DFO**) sobre el grafo. 
    Y luego se ejecuta el recorrido con la función dfs_vertex(...) 
    que realiza un recorrido DF
    """
    search=dfo_search.new_dfo_search()
    search['marked'] =map.new_map(num_elements=g.num_vertices(graph), load_factor=0.75)
    lst_vtcs= g.vertices(graph)
    for i in lt.size(lst_vtcs):    # recorrer todos los vertices
        vertex= lt.get_element(lst_vtcs, i)
        if not map.contains(search['marked'], vertex):
            dfs_vertex(graph, search, vertex)  # iniciar un nuevo recorrido 
    return search


def dfs_vertex(graph, search, vertex):
    """Aplicar el algoritmo DFS desde vertexactualizando los recorridos pre, post, reversepost
        Solución:
        1. Encolar el vertice vertexen la cola search[pre]
        2. Marcar el verticevertexen el mapa search[marked]
        3. Recorrer los adyacentes v de vertex
        3.1    Si el adyacente v No esta marcado en el mapa search[marked]
        3.1.1        Aplicar recursión desde el verticev
        4. Encolar el verticevertexen la cola search[post]
        5. Agregar el verticevertexen el stacksearch[reversepost]6. Retornar search"""
    