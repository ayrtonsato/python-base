# definição ou atribuição
# assinatura + type hints
# documentação / docstring
# código
# valor de retorno, caso não tenha, retorna None

def nome_da_funcao_antigo(a, b ,c): # até os : é a assinatura da função
    """Esta função faz algo com a, b e c.
    
    Use esta função quando quiser a + b + c
    Quando o parâmetro a tiver o valor 10 vai
    acontecer x.
    :param a: Número inteiro
    :type a: int
    :param b: Número inteiro
    :type b: int
    :param c: Número inteiro
    :type c: int
    :return: Retorna o resultado de a + b + c
    """
    return a + b + c

                    # parâmetros
def nome_da_funcao(a: int, b: int , c: int) -> int: # com type hints
    """Esta função faz algo com a, b e c.
    
    Use esta função quando quiser a + b + c
    Quando o parâmetro a tiver o valor 10 vai
    acontecer x.
    
    >>> nome_da_funcao(1, 2, 3)
    6
    """
    return a + b + c

                    # passagem de argumentos posicionais
print(nome_da_funcao(1, 2 , 3))

                    # passagem de argumentos nomeados
print(nome_da_funcao(b = 8, a = 2, c = 10))

                    # passagem de argumentos mista
                    # argumentos posicionais antes dos nomeados
print(nome_da_funcao(1, c = 22, b = 11))



#########################
def outra_funcao(a, b, c):
    """Explica o que a função faz"""
    # tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 =  outra_funcao(1, 2, 3)
print(valor1)
print(valor2)
print(valor3)

valor1_, *resto = outra_funcao(1, 2, 3)
print(valor1_)
print(resto)

############################
# Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz soma de 2 números."""
    return n1 + n2

print(soma(1, 2))
args = (10, 20)
# argumentos em sequência / posicional
print(soma(args[0], args[1]))
print(soma(*args))

args = {"n2": 90, "n1": 100}
print(soma(n1 = args["n1"], n2 = args["n2"]))
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 200, "n1": 100},
    {"n2": 300, "n1": 100},
    [5, 10],
    (2, 3),
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))