#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetNums=[]
soma=0
mult=1
for x in range(5):
    num=int(input("Digite um numero:"))
    vetNums.append(num)

print("\nLista:")

for i in vetNums:
    print(i, end=" ")

for s in vetNums:
    soma+=s

for m in vetNums:
    mult*=m

print("\nSoma:",soma)    
print("Mult:",mult)   
