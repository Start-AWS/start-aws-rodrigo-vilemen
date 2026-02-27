#Ler 5 notas e informar a média (media = (n1+n2+n3+n4+n5)/5).

#Fazendo com o For:
# numero = 0
# soma = 0
# for numero in range(1, 6):
#     nota = float(input("Digite a nota: "))
#     soma += nota

# media = soma/5
# print("Média = ", media)

#Fazendo com o For (Sem declarar o contador, usando apenas um _):
# soma = 0
# for _ in range(1, 6):
#     nota = float(input("Digite a nota: "))
#     soma += nota

# media = soma/5
# print("Média = ", media)

#Fazendo com While: 
soma = 0
numero = 1

while numero < 6:
    nota = float(input(f"Digite a nota {numero}: "))
    soma += nota
    numero += 1

print(f"Média = {soma/5}")