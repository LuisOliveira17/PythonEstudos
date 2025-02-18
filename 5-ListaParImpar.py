#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
x=1
vetorGeral=[]
vetorPar=[]
vetorImpar=[]
for i in range(20):
    resp=int(input(f"Digite o {x}º número:"))
    x+=1
    vetorGeral.append(resp)

    if resp%2==0:
        vetorPar.append(resp)

    elif resp%2!=0:
        vetorImpar.append(resp)

print("\nNúmeros Digitados:",vetorGeral)
print("Impar:",vetorImpar)
print("Par:",vetorPar)