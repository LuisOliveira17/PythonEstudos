salario= int(input("Digite seu salário:"))

if  salario<=280:
    print("Novo salário:" ,round (salario*1.20,2))

elif salario >280 and salario <=700:
    print("Novo salário:" ,round (salario*1.15,2))

elif salario >700 and salario<=1500:
    print("Novo salário:" ,round (salario*1.10,2))


