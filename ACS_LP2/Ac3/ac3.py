
'''
'' Dados os conhecimentos de objetos e dicionários que temos até agora, vamos elaborar
'' um Dicionario para armazenar objetos contendo informações de uma lista telefonica.
'' O dicionário deverá ser criado e armazenado fora do escopo das funções para 
'' ser enviado como parametro para as funções criadas.
''
'''

'''
'' 1. Crie uma classe Contato que tenha os seguintes atributos:
''    nome, telefone, email
''    E também as seguintes operações (métodos):
''    imprime => retorna um string com os valores nome, telefone, email no seguinte formato:
''    nome: {nome}, telefone: {telefone}, email: {email}
''    reset
''    armazena None em cada atributo do objeto
''
''
'''
print('\nExercicio 1\n')

class contato:
    def imprime(self, nome, email, telefone):
        nome = 'Marcio'
        telefone = '46667162'
        email = 'mjpaulino@gmail.com'
        return('Nome: {}, Telefone: {}, Email: {}'.format(nome,telefone,email))
    def rest (self, nome, email, telefone):
            nome = {None}
            telefone = {None}
            email = {None}
            return ('Nome: {}, Telefone: {}, Email: {}'.format(nome,telefone,email))
objeto = contato()
print (objeto.imprime('nome', 'email', 'telefone'))
print (objeto.rest('nome', 'email', 'telefone'))
print ('----------------------------------------')


'''
'' 2. Crie uma função que recebe um dicionario como parametro e retorna a
''    a quantidade de elementos presentes.
''
'''
print('\nExercicio 2\n')
dicionario = {'Nome':'Marcio', 'Sexo':'Masculino', 'Idade':25, 'Cidade':'São Paulo', 'The Originals':'5 Temporadas'}
def conta_elementos(dicionario):
    pass
    return ('A quantidade de elementos presentes no dicionario é de ',len(dicionario))
print (conta_elementos(dicionario))
print ('----------------------------------------')


'''
'' 3. Crie uma função que recebe um dicionário e uma suposta chave como parametro
''    e retorna um booleano informando se aquela chave já está presente no dicionário
''
'''
print('\nExercicio 3\n')
dicionario = {'Nome':'Marcio', 'Sexo':'Masculino', 'Idade':25, 'Cidade':'São Paulo', 'The Originals':'5 Temporadas'}
chave = 'The Originals'
def verifica_presenca(dicionario, chave):
    pass
    existechave = chave in dicionario
    return (existechave)
print (verifica_presenca(dicionario, chave))
print ('----------------------------------------')


'''
'' 4. Crie uma função que recebe um dicionário, uma chave e um objeto como parametros
''    e armazena este objeto no dicionário se ele ainda não existir.
''    Se a informação existir, deverá retornar False
''    Se a informação não existir deverá retornar True
''
'''
print('\nExercicio 4\n')
dicionario = {'Livro': 'A Cabana','Gênero':'Ficção Cientifica',}
chave = 'Livro'
class objeto:
    pass
objeto = objeto()
objeto = 'A Cabana'
def insere(dicionario, chave, objeto):
    contador=0
    pass
    for chaves, valores in dicionario.items():
        if chave == chaves and objeto == valores:
            return False
        else:
            contador += 1    
        if contador == len(dicionario):
            dicionario[chave] = objeto
            print (dicionario)
            return True
print (insere(dicionario, chave, objeto))
print ('----------------------------------------')



'''
'' 5. Crie uma função que recebe um dicionário e uma chave como parametros
''    e remove esta informação do dicionário se ela já existir.
''    Se a informação existir, deverá retornar True
''    Se a informação não existir deverá retornar False
'' 
'''
print('\nExercicio 5\n')
dicionario = {'Nome':'Marcio', 'Sexo':'Masculino', 'Idade':'25', 'Cidade':'São Paulo', 'The Originals':'5 Temporadas'}
chave = 'The Originals'
def remove(dicionario, chave):
    pass
    if chave in dicionario:
        del dicionario[chave]
        return True
    else:
        return False
print (remove(dicionario, chave))
print ('----------------------------------------')


'''
'' 6. Crie uma função que recebe um dicionário como parametro
''    e imprime todos os objetos presentes ordenados pela chave em ordem crescente.
''    (não pode usar a função sort de listas)
''    A saída do console deve ser exatamente:
''    + Iniciando - Imprimindo informacoes do dicionario:
''    chave[valor_da_chave] : valor[nome: {nome}, telefone: {telefone}, email: {email}]
''    ...
''    chave[valor_da_chave] : valor[nome: {nome}, telefone: {telefone}, email: {email}]
''    + Finalizando - Imprimindo informacoes do dicionario:
'''
print('\nExercicio 6\n')
dic_num = {
    17435:"nome: {'Flavio A.'}, telefone: {'222-222'}, email: {'flavio.k@gmail.com'}", 
    17723:"nome: {'Souza V.'}, telefone: {'111-111'}, email: {'souza.@gmail.com'}",
    1778:"nome: {'Otavio B. '}, telefone: {'333-333'}, email: {'otavio.@gmai.com'}",
    178:"nome: {'Luiz E.'}, telefone: {'555-555'}, email: {'luiz@gmai.com'}",   
    }
def imprime(dicionario):
        print("\n+ Iniciando - Imprimindo informações do dicionario:")
        c=0
        x=max(dicionario)+1
        while c != (x):
            for chave, valor in dicionario.items():
                if chave == c :
                    print("chave[{}] : valor[{}]".format(chave,valor))
            c += 1        
        return("+ Finalizando - Imprimindo informações do dicionario:")
print(imprime(dic_num))
print ('----------------------------------------')
