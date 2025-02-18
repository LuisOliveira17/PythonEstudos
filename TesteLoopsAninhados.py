linhas=int(input("Digite o número de linhas:"))
colunas=int(input("Digite o número de colunas:"))
simb=str(input("Digite o símbolo desejado:"))

for x in range(linhas):
    
    for y in range(colunas):
        print(simb, end="")

    print()#Imprime uma nova linha