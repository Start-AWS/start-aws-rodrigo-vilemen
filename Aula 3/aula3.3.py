
n1 = float(input("Digite a nota N1: "))
n2 = float(input("Digite a nota N2: "))
n3 = float(input("Digite a nota N3: "))

media = (n1 + n2 + n3) / 3

if media < 4.1:
    print(f"Média: {media:.2f}")
    print("Aluno REPROVADO")
elif media <= 6.0:
    print(f"Média: {media:.2f}")
    print("Aluno foi para EXAME FINAL")
    
    nota_exame = float(input("Digite a nota do exame: "))
    
    if nota_exame > 6.0:
        print(f"Nota do exame: {nota_exame:.2f}")
        print("Aluno APROVADO")
    else:
        print(f"Nota do exame: {nota_exame:.2f}")
        print("Aluno REPROVADO")
else:
    print(f"Média: {media:.2f}")
    print("Aluno APROVADO")