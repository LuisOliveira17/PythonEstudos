def soma(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundo número:"))
operacao=input("Digite a operação:")

if operacao=="+":
   print(soma(num1,num2)) 

if operacao=="-":
   print(sub(num1,num2)) 

if operacao=="*":
   print(mult(num1,num2)) 

if operacao=="/":
   print(div(num1,num2)) 