def new_prim_search(source):
    """
    Crea una estructura de busqueda usada en el algoritmo **prim**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de inicio del MST.
    - **edge_to**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **dist_to**: Mapa con las distancias a los vertices. Se inicializa en ``None``
    - **marked**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola de prioridad indexada (index_priority_queue). Se inicializa en ``None``
    - **mst**: Cola con los vertices visitados en postorden inverso. Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: prim_search
    """

    search = {
        "source": source,
        "edge_to": None,
        "dist_to": None,
        "marked": None,
        "pq": None,
        "mst": None,
    }
    return search
