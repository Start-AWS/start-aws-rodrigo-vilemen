# # Tipo Inteiro:

# # num = 3
# # numInteiro = 10
# # num_convidados = 20
# # numNegativo = -30

# # Tipo Float:

# # pi = 3.14
# # peso = 85.5
# # preco = 39.90

# # Tipo texto (String)

# # letra = "a"
# # linguagem = "Minha linguagem de programação favorita é Python"
# # texto = "qualquer texto aqui.."
# # texto2 = 'dasdasdasdad'
# # texto3 = " Ele disse que era 'Bonito'\ndsasadasdad"
# # linguagemFavorita = "Java"

# # print("Minha linguagem de programação favorita é", linguagemFavorita)

# # Entrada de dados (input)

# # idade = input("Qual a sua idade: ")
# # print("Sua idade é: ", idade)


# # Faça um programa que solicite dois números e imprima a soma

# # num1 = int(input("Insira um número: "))
# # num2 = int(input("Insira outro número: "))
# # print("Resultado = ", num1 // num2)

# #Faça um programa para calcular a distância efetuada em uma viagem e quantos litros foram usados, de gasolina, para efetuar a viagem. Fórmulas: distância = tempo (h)* velocidade (km/h),              litros_usados = distancia / consumo

# # tempo = float(input("Digite o tempo gasto na viagem: "))
# # velocidade = float(input("Digite a velocidade média: "))
# # consumo = float(input("Digite o consumo do carro: "))

# # distancia = tempo * velocidade
# # litros_usados = distancia / consumo

# # print("Distância = ", distancia)
# # print("Quantidade de litros = ", round(litros_usados, 2))

# # Manipulação de String

# a = "casaco"
# print(a)

# #Colocar a variável em maiúsculo
# print(a.upper())

# #Colocar a variável em minúsculo
# print(a.lower())

# #Colocar somente a primeira letra maiúscula
# print(a.capitalize())

# #Pegar uma parte da palavra
# print(a[0:2])

# #Pegar todas as letras a partir de uma posição
# print(a[3:])

# #Substituir parte da palavra por outra
# print(a.replace("aco", "inha"))

# #Encontrar o índice de um caractere
# print(a.find("s"))
# print(a.find("a"))
# print(a.find("z")) #quando não encontra a posição existente retorna '-1'

# #Retornar o tamanho da string
# print(len(a))

# #Retirar espaço em branco de uma string
# b = "             Eu sou Felipe"
# print(b.strip())

##Fazendo a potência de um número com a biblioteca Math
import math
num = 5
print(num**2)
print(pow(num, 2))

##Fazendo a raiz quadrada através da biblioteca Math
num2 = 25
print(num2**(1/2))
print(math.sqrt(num2))