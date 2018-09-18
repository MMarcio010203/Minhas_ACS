
lista = [12345678, 25474817, 85400458]
telefone = 25474817

def verifica_presenca(lista, telefone):    
    buscador = 0
    while buscador < len(lista):
        if telefone == lista[buscador]:
            return "O telefone está na lista"
        if buscador == 2:
            if telefone != lista[buscador]:
                return "O telefone não está presente na lista"
            buscador = buscador + 1
            
print(verifica_presenca(lista, telefone))
