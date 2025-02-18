class Carro:
    def apresentarModelo(informacao):
        print("Modelo:"+ informacao.modelo)
        print("Cor:"+ informacao.cor)
        print("Acessórios:"+ informacao.acessorios)

especificacoes = Carro() #Instanciar a classe em uma variável

especificacoes.modelo="Monza"
especificacoes.cor="Roxo"
especificacoes.acessorios="Aerofólio"

especificacoes.apresentarModelo()

especificacoes2= Carro()
especificacoes2.modelo="Gol Quadrado"
especificacoes2.cor="Branco"
especificacoes2.acessorios="Body Kit completo"
print("\n")
especificacoes2.apresentarModelo()