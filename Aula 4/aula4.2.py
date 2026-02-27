#Escreve um programa que receba dois números (início e fim de um intervalo) e conte quantos números pares existem nesse intervalo.

# Operador MOD (%): Pega o resto da divisão de números inteiros
# 10/3 = 3 (sobra 1)
# 10%3 = 1 (pegou a sobra no resultado)
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

contPares = 0
for numero in range(inicio, fim+1):
    if numero % 2 == 0:
        #pares = pares + 1
        contPares += 1
    
print(contPares)