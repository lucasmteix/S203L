from Filme import Filme
from Catalogo import Catalogo

# DECLARACAO DE VARIAVEIS

catalogo0 = Catalogo() # objeto que organizara os filmes do catalogo

#Variaveis de entrada

codigo_operacao = -1 # codigo para indicar qual operacao o usuario quer fazer

# Variaveis auxiliares

flag = "S" # flag para controlar o loop principal. S para sim (rodar) e N para não (não rodar)

# Filmes pre cadastrados

filme0 = Filme("Um Sonho de Liberdade", 1994, "Frank Darabont", "Drama", (2*60+22))
filme1 = Filme("O Poderoso Chefão", 1972, "Francis Ford Copolla", "Drama", (2*60+55))
catalogo0.filmes.append(filme0)
catalogo0.filmes.append(filme1)




# Loop principal

# Imprimindo um texto de boas-vindas para o usuario
print("Bem-vindo(a) ao catálogo de filmes.") # texto de boas-vindas

while flag == "S":

    # Imprimindo textos de instrucao para o usuario
    print("Digite o código respectivo à operação que deseja realizar:") # texto de instrucao
    print("1 - cadastrar um novo filme no catálogo") # texto de instrucao
    print("2 - listar os filmes cadastrados") # texto de instrucao

    codigo_operacao = int(input()) # fazendo a entrada do codigo de operacao

    #Estrutura de decisao para fazer a operacao de acordo com o codigo de operacao
    if codigo_operacao == 1:

        # Imprimindo textos de indicacao para o usuario
        print("Você escolheu a operação cadastrar um novo filme no catálogo.") # texto de indicacao
        print("Adicionando um novo filme ao catálogo...") # texto de indicacao
        catalogo0.cadastrar_filme() # fazendo o cadastro do filme
    elif codigo_operacao == 2:

        # Imprimindo textos de indicacao e instrucao para o usuario
        print("Você escolheu a operação listar os filmes cadastrados.") # texto de indicacao
        print("Listando os filmes cadastrados...") # texto de indicacao

        # Imprimindo textos de instrucao sobre ordenacao para o usuario
        print("Você deseja que os filmes sejam ordenados de alguma maneira específica?") # texto de instrucao
        print('Digite "S" para sim e "N" para não.') # texto de instrucao

        codigo_ordenacao = input() # fazendo a entrada do codigo de ordeancao

        #Estrutura de decisao para definir o parametro de ordenacao
        if codigo_ordenacao == "S": # caso se deseje ordenar a lista, faz-se a entrada do parametro de ordenacao

            print("Qual parâmetro você deseja usar para ordenar os filmes do catálogo?") # texto de instrucao
            print("Digite ano_de_lancamento para ano, genero para gênero e nome_diretor para diretor") # texto de instrucao
            parametro_ordenacao = input() # fazendo a entrada do parametro de ordencao
        else: # caso nao se deje ordenar a lista, parametro_ordenacao eh definido como None
            parametro_ordenacao = None
        
        # Imprimindo textos de instrucao sobre filtragem para o usuario
        print("Você deseja que os filmes sejam filtrados?") # texto de instrucao
        print('Digite "S" para sim e "N" para não.') # texto de instrucao

        codigo_filtragem = input() # fazendo a entrada do codigo de filtragem

        #Estrutura de decisao para definir o parametro de filtragem e o valor de filtragem
        if codigo_filtragem == "S": # caso se deseje filtrar a lista, faz-se a entrada do parametro de filtragem e do valor de filtragem

            print("Qual parâmetro você deseja usar para filtrar os filmes do catálogo?") # texto de instrucao
            print("Digite ano_de_lancamento para ano, genero para gênero e nome_diretor para diretor") # texto de instrucao
            parametro_de_filtragem = input() # fazendo a entrada do parametro de ordencao

            print("Qual valor você deseja usar para filtrar os filmes do catálogo?") # texto de instrucao
            print("Digite o valor desejado") # texto de instrucao
            valor_filtragem = input() # fazendo a entrada do parametro de ordencao
        else: # caso nao se deje filtrar a lista, parametro_ordenacao eh definido como None
            parametro_de_filtragem = None
            valor_filtragem = None
        
        catalogo0.imprimir_lista(parametro_ordenacao, 
                                 parametro_de_filtragem, 
                                 valor_filtragem) # imprimindo a lista de acordo com o que foi escolhido pelo usuario
    else:
        print("Codigo não reconhecido.")

    # Imprimindo textos de instrucao para o usuario
    print("Deseja realizar mais operações?") # texto de instrucao
    print('Digite "S" para sim e "N" para não (fechar o catálogo).') # texto de instrucao

    flag = input() # entrada da flag para poder decidir entre continuar ou nao o loop principal

    # Estrutura de decisao para possivelmente quebrar o loop principal caso a flag seja igual a "N"
    if flag == "N":
        break