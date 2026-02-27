#Imagine que você queira imprimir de 1 a 5:
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

#Estrutura de repetição For:
# for numero in range(1, 6):
#     print(numero)

# print("fim do programa!")

#Escrevendo For em ordem decrescente de -1 (passo -1):
# for numero in range(5, 0, -1):
#     print(numero)

#Escrevendo For somente números pares (passo 2):
# for numero in range(0, 51, 2):
#     print(numero)

#Somando todos os números pares de 0 até 50, e imprimindo o resultado:
# soma = 0
# for numero in range(0, 51, 2):
#     soma = soma + numero

# print(soma)

#Imprimir letra por letra, em seguida procurar a letra Q:
# palavra = "Chocolate Quente"
# for letra in palavra:
#     print(letra)
#     if letra == "o":
#         print("Achou a letra o")
#         break

# print("Fim")
# print("do")
# print("Programa")

#Loop "Sabor" Infinito (EVITE FAZER ISSO!):
# for numero in range(0, 10000000000000000000000000000000000000000):
#     print(numero)

#Usar o For aninhado:
for num1 in range(1, 5):
    print(num1)
    print("-----")
    for num2 in range(0, 3):
        print(num2)
    print()