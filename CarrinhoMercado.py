listacomidas=[]
listaprecos=[]
precofinal=0

while True:

    comida=str(input("Digite o nome da comida:"))
    if comida.lower()=="q":
        break
   
    else:
        listacomidas.append(comida)
        precos=float(input(f"Agora digite o preço do alimnento {comida}:"))
        listaprecos.append(precos)



print("\n---Lista de Compras---")

for x in listacomidas:
    print(x, end=" ")

for p in listaprecos:
    precofinal+=p

print("\n---Preço:---")
print("R$:",precofinal)