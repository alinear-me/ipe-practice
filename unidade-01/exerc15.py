import math

cateto1 = float(input("Digite o tamnaho do primeiro cateto:"))

cateto2 = float(input("Digite o tamnaho do segundo cateto:"))

hipotenusa = (cateto1 ** 2) + (cateto2 ** 2)
raiz = math.sqrt(hipotenusa)

print("O valor da hipotenusa é: ", raiz)