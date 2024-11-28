import array_list as lt
def new_cola():
    return lt.new_list()

def encolar(cola,elemento):
    #if cola ==None:
    #    cola=new_cola() esto es por si necesitamos hacer ese filtro pero creo que mejor se implemente en los cositos 
    return lt.add_last(cola,elemento)


def desencolar(cola):
    return lt.remove_first(cola)

def primer_elemento(cola):
    return lt.first_element(cola)

def is_empty(cola):
    return lt.is_empty(cola)

def size(cola):
    return lt.size(cola)
