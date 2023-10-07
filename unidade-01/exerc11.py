# 11. Agora, construa um programa que solicite ao usuário a temperatura em graus Celsius 
# e a transforme em Fahrenheit. Mostre o resultado na tela.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = ((9/5) * celsius) + 32

print("A temperatura em Fahrenheit é: %.2f" %  fahrenheit)