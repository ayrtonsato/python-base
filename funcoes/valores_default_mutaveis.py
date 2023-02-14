# set, dict, list -> mutaveis
def adiciona_a_lista(valor, lista = None):
    # caso não faça isso,
    # ele cria uma lista uma vez só
    # e reutiliza a mesma lista
    if lista is None:
        lista = [] 
    lista.append(valor)
    return lista

adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))