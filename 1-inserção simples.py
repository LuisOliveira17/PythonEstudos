listaVazia=[]
x=1

for i in range(1,6):
    resposta=int(input(f"Digite o {x}º número:"))
    listaVazia.append(resposta)
    x+=1

print("Lista:")
for y in listaVazia:
    print(y)


print("Lista Inversa:")
listaVazia.reverse()
for u in listaVazia:
    print(u)
    
