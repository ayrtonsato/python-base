contador =  0

def incrementa_contador():
    # quando houver assignment
    # python espera que exista uma variável local
    # contador += 1
    global contador
    contador += 1
    
incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)