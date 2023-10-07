# Crie um programa em Python que solicite ao usuário dois números inteiros e imprima o
# maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if (num1 > num2):
    print("O número", num1, " é maior que o número ", num2)
elif (num2 > num1):
    print("O número", num2, " é maior que o número ", num1)
else:
    print("Números iguais!")