from Filme import Filme

class Catalogo:

    """Classe que representa o catálogo de filmes"""




    #Construtor
    def __init__(self):
        self.filmes = []
    



    # Metodos
    
    # Metodo que realiza a entrada das infos de um novo filme e o cadastra no catalogo
    def cadastrar_filme(self):

        print("Adicionando um filme...") # texto de indicacao
        titulo = input("Insira o título do filme: ") # entrada do titulo do filme
        ano_de_lancamento = int(input("Insira o ano de lançamento do filme: ")) # entrada do ano de lancamento do filme
        nome_diretor = input("Insira o nome do diretor do filme: ") # entrada do nome do diretor do filme
        genero = input("Insira o gênero do filme: ") # entrada do genero do filme
        duracao = int(input("Insira a duração do filme: ")) # entrada da duracao do filme
        novo_filme = Filme(titulo, ano_de_lancamento, nome_diretor, genero, duracao)
        self.filmes.append(novo_filme)
    
    # Metodo que imprime as informacoes dos filmes da lista passada
    def imprimir_lista(self, parametro_ordenacao, parametro_de_filtragem, valor_filtragem):

        lista_a_imprimir = self.filmes # inicialmente, a lista a ser impressa eh igual aa lista filmes

        if(parametro_ordenacao != None):
            lista_a_imprimir = self.criar_lista_reodernada(lista_a_imprimir, parametro_ordenacao)
        
        if((parametro_de_filtragem != None) and (valor_filtragem != None)):
            lista_a_imprimir = self.criar_lista_filtrada(lista_a_imprimir, parametro_de_filtragem, valor_filtragem)
            

        #Estrutura de repeticao para percorrer a lista
        for filme in lista_a_imprimir:

            filme.imprimir_info_filme() # imprimindo as informacoes do filme na tela
            print() # linha de quebra

    # Metodo para criar uma nova lista reodernada crescentemente por algum parametro
    def criar_lista_reodernada(self, lista_filmes, parametro_de_ordenacao):

        lista_reodernada = sorted(lista_filmes, 
                                  key=lambda x: getattr(x, parametro_de_ordenacao), 
                                  reverse=False) # reodernando a lista
        
        return lista_reodernada # retornando a lista reodernada
    
    # Metodo para criar uma nova lista filtrada por um paramatreo
    def criar_lista_filtrada(self, lista_filmes, parametro_de_filtragem, valor_filtragem):

        lista_filtrada = [] # criando a lista filtrada vazia

        # Estrutura de repeticao para adicionar aa lista filtrada apenas filmes que correspondam aa filtragem
        for filme in lista_filmes:
            if getattr(filme, parametro_de_filtragem) == valor_filtragem:
                lista_filtrada.append(filme)
        
        return lista_filtrada # retornando a lista filtrada