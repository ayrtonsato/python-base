# escopo built-in maior que o Global
# começa o escopo global
nome = "Global"
numero = 1

def funcao():
    # aqui começa o escopo local
    nome = "Local"
    # consigo chamar uma variável de um escopo maior
    # ou envolvente
    # print(numero)
    
    def funcao_interna(): # inner function / closure
        # começa o escopo local da função interna
        nome = "Interna"
        print("Escopo local da função interna: ", locals())
        print(nome)
        print("*" * 30)
        return nome
        # termina o escopo local da função interna    
    
    funcao_interna()
    # print variáveis locais
    print("Escopo local da função: ", locals())
    print("ESSA VEM DA FUNCAO: ", nome)
    
    return nome
    # aqui termina o escopo local

# print as variáveis globais
print("Variaveis globais: ", globals())
print("-" * 30)

funcao()
print(nome)

# termina o escopo global