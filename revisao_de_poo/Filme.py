class Filme:

    """Classe que representa um filme"""




    # Construtor
    def __init__(self, titulo, ano_de_lancamento, nome_diretor, genero, duracao_em_minutos):
        
        self.titulo = titulo # titulo do filme (string)
        self.ano_de_lancamento = ano_de_lancamento # ano de lancamento do filme (int)
        self.nome_diretor = nome_diretor # nome do diretor do filme (string)
        self.genero = genero # genero do filme (stirng)
        self.duracao_em_minutos = duracao_em_minutos # duracao do filme em minutos (int))




    # Metodos
    
    # Metodo para converter a duracao em minutos do filme para uma string no formato xhymin
    def converter_formato_duracao(self, duracao_em_minutos):

        horas_inteiras = duracao_em_minutos//60
        minutos_restantes = duracao_em_minutos - horas_inteiras*60
        duracao_formato_xhymin = str(horas_inteiras) + "h" + str(minutos_restantes) + "min"
        return duracao_formato_xhymin

    # Metodo que imprime as informacoes de um filme na tela
    def imprimir_info_filme(self):

        print('Título: "' + self.titulo + '"') # imprimindo o titulo do filme na tela
        print("Ano de lançamento:", self.ano_de_lancamento) # imprimindo o ano de lancamento do filme na tela
        print("Diretor:", self.nome_diretor) # imprimindo o nome do diretor na tela
        print("Gênero:", self.genero) # imprimindo o gênero do filme na tela
        print("Duração:", self.converter_formato_duracao(self.duracao_em_minutos)) # imprimindo a duracao do filme na tela