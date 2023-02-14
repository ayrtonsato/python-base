# Não esquecer do S do SOLID - Single Responsability
def funcao(*args, timeout = 10, **kwargs):
    for item in args:
        print(item)
    print(kwargs)
    print(f"timeout {timeout}")
    
# respeitar a ordem
# primeiro os argumentos sem nomes (posiocionais)
# e depois os nomeados
funcao(
    "Ayrton",
    1,
    True,
    [],
    timeout=20,
    nome = "Ayrton",
    idade = 31,
)