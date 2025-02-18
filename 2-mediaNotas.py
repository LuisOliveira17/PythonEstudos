#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
x=1
nota=[]
media=0
for i in range(1,6):
    resp=int(input((f"Digite a {x}º nota:")))
    nota.append(resp)
    media+=resp
    print("Média:",media)
    x+=1

print("As notas foram:")
for y in nota:
 print(y)

print("Média:",media/(x-1))    