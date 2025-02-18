"""
class Pessoa:
    def pessoaDados(dado):
        print("\nDados de registro:")
        print("Nome:"+dado.nome)
        print("Telefone:"+dado.telefone)
        print("Cargo:"+dado.cargo)

respostas=Pessoa()

respostas.nome=input("Digite seu nome:")
respostas.telefone=input("Digite seu telefone:")
respostas.cargo=input("Digite seu cargo:")

respostas.pessoaDados()
"""
#Ou
 
class Pessoa:
    def pessoaDados(dado,nome,telefone,cargo):
        dado.nome=nome
        dado.telefone=telefone
        dado.cargo=cargo

        print(dado.nome,dado.telefone,dado.cargo)

resposta=Pessoa()

resposta.pessoaDados("Luis",19338412,"Balconista")