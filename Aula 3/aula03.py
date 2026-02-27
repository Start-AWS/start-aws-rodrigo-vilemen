# Operadores lógicos
a = True
b = False
# print(a, b)

#Sentenças
#Condições para ir na aula presencial do Start
# x = ônibus funcionando
# y = sem chuva

#Tabela Verdade "OU (Or)" Só é FALSO quando tudo for FALSO.
# | x | y | Resultado |
# | V | V |     V     |
# | V | F |     V     |
# | F | V |     V     |
# | F | F |     F     |


#Tabela Verdade "E (And)" Só é VERDADEIRO quando tudo for VERDADEIRO.
# | x | y | Resultado |
# | V | V |     V     |
# | V | F |     F     |
# | F | V |     F     |
# | F | F |     F     |

#Tabela Verdade "Não (Not)"
# | x | Resultado |
# | V |     F     |
# | F |     V     |


# print(a and b) #no lugar do and posso usar &
# print(a or b) #no lugar do or posso usar |
# print(not a)

#Operadores relacionais
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 <= 3)
print(5 == 3)
print(5 != 3)


idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
else:
    print("Adulto")3