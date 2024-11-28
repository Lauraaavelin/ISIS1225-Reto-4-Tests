from ..Map import map_functions as ma
from ..Map import map_entry as me
from ..List import array_list as lt
import random

def new_map(num_elements, load_factor, prime=109345121):
    pass
    #parfa el mapa vamos a  hacer un diccionario que contenga los valores que requerimos 
    # con una clase se puede hacer que cuando entre un elñemento se pueda modificar dentro de si mismo para eso se usa el self 
    #con el atributo init_ se llama cuando creas una instancia de uhna clase y su proposito es iniciar los atributos del objeto recien creado 
    capacity = ma.next_prime(int(num_elements / load_factor))
    
    # Generar valores aleatorios para 'scale' y 'shift' estos se4 usan en la funcion del hash 
    scale = random.randint(1, prime - 1) 
    shift = random.randint(0, prime - 1)
    
    # Crear la tabla vacía
    table=lt.new_list()
    elementos = [None] * capacity
    table["elements"]=elementos 
    table["size"]=capacity
    # Crear el mapa (diccionario) que contendrá todos los atributos
    map_linear_probing = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,  # Factor de carga actual, inicializado en 0
        'limit_factor': load_factor,  # Factor de carga máximo de la tabla
        'size': 0,  # Número de elementos en la tabla
        'type': "PROBING"  # Tipo de tabla de sondeo lineal
    }
    
    return map_linear_probing


def default_compare(key1, key2):
    """
    Función de comparación por defecto. Retorna True si las llaves son iguales, False en caso contrario.
    """
    return key1 == key2

def is_available(table, pos):
    """
    Informa si la posición pos esta disponible en la tabla de hash.
    Se entiende que una posición está disponible
    si su contenido es igual a None (no se ha usado esa posicion)
    o a __EMPTY__ (la posición fue liberada)
    """
    entry = lt.get_element(table, pos)
    if (entry['key'] is None or entry['key'] == '__EMPTY__'):
            return True
    return False



def hash_function(key, map_info):
    prime = map_info['prime']
    scale = map_info['scale']
    shift = map_info['shift']
    capacity = map_info['capacity']
    
    return ((scale * hash(key) + shift) % prime) % capacity


def put(map_info, key, value):
    capacity = map_info['capacity']
    table = map_info['table']["elements"]
    
    index = hash_function(key, map_info)
    original_index = index
    start = True
    
    # Sondeo lineal para encontrar un índice vacío o actualizar uno existente
    while table[index] is not None:
        if table[index][0] == key:
            # Reemplazar valor si ya existe la clave
            table[index] = (key, value)
            return
        index = (index + 1) % capacity
        if index == original_index and not start:
            raise Exception("Tabla está llena")
        start = False

    # Insertar nueva clave y valor
    table[index] = (key, value)
    map_info['size'] += 1
    map_info['current_factor'] = map_info['size'] / capacity

    # Verificar si es necesario redimensionar
    if map_info['current_factor'] > map_info['limit_factor']:
        resize(map_info)
        

def is_empty(map_info):
    return map_info['size'] == 0    
   
        
def next_prime(n):
    """ Devuelve el siguiente número primo mayor que n """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prime = n
    while True:
        prime += 1
        if is_prime(prime):
            return prime

def resize(map_info):
    old_table = map_info['table']["elements"]
    new_capacity = next_prime(map_info['capacity'] * 2)
    
    # Redimensionar el mapa
    map_info['capacity'] = new_capacity
    table=lt.new_list()
    elem=[None] * new_capacity
    table["elements"]=elem
    table["size"]=new_capacity
    map_info['table'] = table
    map_info['size'] = 0  # Vamos a reinsertar, así que volvemos a 0

    # Reinserción de los elementos en la nueva tabla
    for entry in old_table:
        if entry is not None:
            key, value = entry
            put(map_info, key, value)
            
        
   
def contains(my_map, key):
    capacity = my_map['capacity']
    index = ma.hash_value(my_map, key)  # Obtener el índice inicial usando la función hash
    probing = 0  # Contador para el sondeo
    # Realizar la búsqueda mediante sondeo lineal
    while probing < capacity:
        pos = (index + probing) % capacity  # Ajuste de posición con sondeo lineal
        if my_map['table']["elements"][pos] is None:
            return False  # Si encontramos un espacio vacío, la llave no está
        if my_map['table']["elements"][pos][0] == key:
            return True  # Si encontramos la llave, retornamos True
        probing += 1  # Continuamos con el siguiente índice
    
    return False
    
    
def size(my_map):
    return my_map["size"]



def value_set(my_map):
    lista= lt.new_list()
    for tupla in my_map["table"]["elements"]:
        if tupla is not None :
            valor= tupla[1]
            if valor !='__EMPTY__':
                lt.add_last(lista,valor)
    
    return lista


def rehash(my_map):
    old_table = my_map['table']["elements"]  
    old_capacity = my_map['capacity']
    
   
    new_capacity = ma.next_prime(2 * old_capacity)
    
    table=lt.new_list()
    ele=[None] * new_capacity
    table["elements"]=ele
    my_map['table'] = table
    my_map['capacity'] = new_capacity
    my_map['size'] = 0  
    
    for entry in old_table:
        if entry is not None:  
            key, value = entry
            put(my_map, key, value) 
    
    return my_map
        

def get(my_map, key):
    capacity = my_map["capacity"]
    index = ma.hash_value(my_map, key)
    probing = 0

    while probing < capacity:
        pos = (index + probing) % capacity
        if my_map["table"]["elements"][pos] is None:
            return None
        if my_map["table"]["elements"][pos][0] == key:
            return my_map["table"]["elements"][pos][1]
        probing += 1

    return None
    

def find_slot(map_info, key, hash_value):
    table = map_info["table"]["elements"]
    capacity = map_info["capacity"]
    index = hash_value % capacity
    probing = 0
    first_empty = None
    
    while probing < capacity:
        pos = (index + probing) % capacity
        entry = table[pos]
        
        if entry is None:
            return False, first_empty if first_empty is not None else pos
        if entry[0] == key:
            return True, pos
        if entry[0] == '__EMPTY__' and first_empty is None:
            first_empty = pos 
        probing += 1
    
    return False, first_empty


def remove(my_map, key):
    # Obtener la capacidad de la tabla hash
    capacity = my_map["capacity"]
    # Calcular el índice inicial con la función hash
    index = ma.hash_value(my_map, key)
    probing = 0  # Inicializar la variable de sondeo

    # Iterar mientras no se supere la capacidad de la tabla
    while probing < capacity:
        # Obtener la posición actual aplicando sondeo lineal
        pos = (index + probing) % capacity

        # Si encontramos una casilla vacía, la clave no está en la tabla
        if my_map["table"]["elements"][pos] is None:
            return None
        
        # Verificar si la clave en la posición actual es la que buscamos
        if my_map["table"]["elements"][pos][0] == key:
            # Marcar la posición como vacía y reducir el tamaño del mapa
            my_map["table"]["elements"][pos] = ('__EMPTY__', '__EMPTY__')
            my_map["size"] -= 1
            return my_map
        
        # Continuar con el sondeo lineal si no se ha encontrado la clave
        probing += 1

    # Si se ha recorrido toda la tabla sin encontrar la clave, retornar None
    return None



def is_available(table, pos):
    """
    Informa si la posición `pos` está disponible en la tabla de hash.
    La posición está disponible si es `None` o ha sido marcada como `__EMPTY__`.
    """
    entry = table["elements"][pos]
    if (entry is None )or (entry== ('__EMPTY__','__EMPTY__')):
        return True
    return False

def key_set(my_map):
    lista = lt.new_list()
    for tupla in my_map["table"]["elements"]:
        if tupla is not None :
            valor= tupla[0]
            if valor !='__EMPTY__':
                lt.add_last(lista,valor)

    return lista