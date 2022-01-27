arq = open('registrados.txt', 'a')
print('Olá, aqui você pode adicionar uma nova conta!')
nome_usuario = input('Digite o nome de usuário: ')

arq.write('{}\n'.format(nome_usuario))
'''
Adição da constante \n new line
Uma vez que write não o adiciona automaticamente
'''

print('Cadastro realizado com sucesso!\n')
arq.close() #O arquivo é fechado do modo de adição para ser aberto
            #posteriormente no modo de leitura

arq = open('registrados.txt') #abrindo no modo de leitura
print('Efetue o seu login')
nome_login = input('Digite o seu nome de usuario: ')

registrados = arq.readlines()
if nome_login + '\n' in registrados:
    print('Bem vindo, {}!'.format(nome_login))
else:
    print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')


books = [ 
       {"book": "Como eu nasci?", "stage": 5, "classificacao": 18},
       {"book": "A estrela de belem", "stage": 80, "classificacao": "L"},
       {"book": "O jogo da imitação", "stage": 90, "classificacao": 12}
    ]
book = None
find = str(input("Digite o nome do livro e irei dizer as informação na biblioteca: "))

for i in books:
    if i["book"] == find:
        book = i
        break;
if book is None:
    print("Eu não encontrei o livro que você deseja!")
else:
    print(f'O livro {book["book"]} se encontra na prateleira {book["stage"]} com classificação de {book["classificacao"]} anos')

#ainda tem alguns erros mas vou arrumar ao tempo n fiz o sistema de login ai so tem o sistema de cadastro e procurar
