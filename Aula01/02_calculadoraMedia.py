# -*- coding: UTF-8 -*-

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) / 2

if (media >= 7):
    print(f"O aluno obteve a média {media:.2f} e está Aprovado")
else:
    print(f"O aluno obteve a média {media:.2f} e está Reprovado")


