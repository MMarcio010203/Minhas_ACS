lista = [123456789, 271827349, 6529837654]
telefone = 271827349

def verifica_prest(lista, telefone):
    buscador = 0
    while buscador < len(lista):
        if telefone == lista[buscador]:
            return "O Telefone contido na lista"
        if buscador == 2:
            if telefone != lista[buscador]:
                return "O telenone não encontrado na lista"
                buscador = buscador + 1
                
print(verifica_prest(lista, telefone))
                                  

