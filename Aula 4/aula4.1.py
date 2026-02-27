#Faça um programa que solicite um número e mostre a tabuada desse número de 1 a 10:

numero = int(input("Digite o número da tabuada: "))

for a in range(1, 11):
    #print(numero, "x", a, " = ", numero*a)
    print(f"{numero} x {a} = {numero*a}")