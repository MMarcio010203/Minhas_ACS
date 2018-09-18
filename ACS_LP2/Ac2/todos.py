'''
'' Dados os conhecimentos de listas que temos até agora, vamos elaborar
'' uma lista para armazenar informações de telefones.
'' A lista deverá ser criada e armazenada fora do escopo das funções para 
'' ser enviada como parametro para as funções criadas.
'' Não utilizar as funções de lista (sort, max, min)
'''
'''
'' 1. Crie uma função que recebe uma lista como parametro e retorna a
''    a quantidade de elementos presentes.
'''

lista = [10065439, 45424278, 76854354, 98767645]

def conta_elementos(lista):
    return "Quantidade de elementos na lista: \n{} elementos encontrados".format(len(lista))

print(conta_elementos(lista))

'''
'' 2. Crie uma função que recebe uma lista e um suposto telefone
''    e retorna um booleano informando se aquele telefone já está presente na lista
'''


lista = [25487596, 54875956, 548762458]
telefone = 54875956

def verifica_presenca(lista, telefone):     
    buscando = 0
    for buscando in range (0,len(lista)):
        if lista[buscando] == telefone:
            return "Este telefone consta 4na lista"
        if buscando == 2:
            if telefone != lista[buscando]:
                return "Este telefone não consta na lista"
        buscando = buscando + 1
    
print(verifica_presenca(lista, telefone))

'''
'' 3. Crie uma função que recebe uma lista e um telefone como parametros
''    e armazena esta informação na lista se ela ainda não existir.
''    Se a informação existir, deverá retornar False
''    Se a informação não existir deverá retornar True
'''

lista = [25487596, 54875956, 548762458]
telefone = int(input('Digite o número de telefone: \n'))

def insere(lista, telefone):
    informacao = 0
    for informacao in range(0,len(lista)):
        if telefone == lista[informacao]:
            return False
        if informacao == 2:
            if telefone != lista[informacao]:
                lista.append(telefone)
                return True
        informacao = informacao + 1
print (insere(lista, telefone))

'''
'' 4. Crie uma função que recebe uma lista e um telefone como parametros
''    e remove esta informação da lista se ela já existir.
''    Se a informação existir, deverá retornar True
''    Se a informação não existir deverá retornar False
'''

lista = [25487596, 54875956, 548762458]
telefone = int(input('Digite o número de telefone: \n'))

def remove(lista, telefone):
    informacao = 0
    for informacao in range(0,len(lista)):
        if telefone == lista[informacao]:
            del(lista[informacao])
            return True
        if informacao == 2:
            if telefone != lista[informacao]:
                return False
        informacao = informacao + 1
print (remove(lista, telefone))

'''
'' 5. Crie uma função que recebe uma lista como parametro
''    e imprima todos os dados presentes no console de forma ordenada (sem usar sort).
''    A saída do console deve ser exatamente:
''    + Iniciando - Imprimindo informacoes da lista:
''    índice[valor_do_indice] : valor[valor_armazenado_no_índice]
''    índice[valor_do_indice] : valor[valor_armazenado_no_índice]
''    + Finalizando - Imprimindo informacoes da lista:
'''
lista = [25487596, 54875956, 548762458]

def imprime(lista):
    print("+ Iniciando - Imprimindo Informação da lista:")
    for informacao in range(len(lista)):
        for telefone in range(len(lista) -1):
            if lista[telefone]> lista[telefone + 1]:
                lista[telefone],lista[telefone +1] = lista[telefone + 1], lista[telefone]
            print("{} : {}" .format(telefone,lista[telefone]))
    print("+ Imprimindo Informações da Lista:")
    return " lista em ordem numerica - > {}" .format(lista)

print(imprime(lista))
