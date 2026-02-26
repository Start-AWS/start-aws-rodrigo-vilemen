# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# print("Escolha a operação:")
# print("1 - Soma")
# print("2 - Subtração")

# operacao = input("Digite 1 ou 2: ").strip()

# if operacao == "1":
#     resultado = num1 + num2
#     print(f"Resultado da soma: {resultado}")
# elif operacao == "2":
#     resultado = num1 - num2
#     print(f"Resultado da subtração: {resultado}")
# else:
#     print("Opção inválida, reiniciando programa.")

idade = int(input("Digite sua idade: "))
if idade < 0:
        print("Idade inválida.")
elif idade <= 12:
        print("Criança")
elif idade <= 17:
        print("Adolescente")
else:
        print("Adulto")