#Estrutura de repetição While (enquanto):
# numero = 1
# while numero < 6:
#     print(numero)
#     numero += 1

# print("Fim do programa")

#Loop infinito (EVITE FAZER ISSO!!)
# numero = 1
# while numero < 6:
#     print(numero)
#     #numero += 1

# print("Fim do programa")

import os

resposta = "s"
while resposta.lower() == "s":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    soma = num1 + num2
    print("Soma = ", soma)

    resposta = input("Deseja efetuar uma nova operação?\nDigite 's' para continuar ou qualquer tecla para encerrar:  ")

    os.system('cls')

print()
print("Fim do programa!")