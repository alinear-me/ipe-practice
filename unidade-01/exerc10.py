# Construa um programa que solicite a temperatura em graus Fahrenheit ao usuário e 
# transforme a temperatura em graus Celsius. Imprima na tela. Dica:

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)

print("A temperatura em graus Celsius é: %.2f" % celsius, "º.")