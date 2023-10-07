N1 = int(input("Digite o primeiro número (INT): ")) 
N2 = int(input("Digite o segundo número (INT): "))
N3 = int(input("Digite o terceiro número (INT): "))

resto = N1 % N2
expo = N2 ** N3
div = (N1 / N3) + N2

print(" o resto da divisão do primeiro com o segundo: ", resto)
print(" o segundo exponencial com o terceiro: ", expo)
print(" o primeiro dividido pelo terceiro, somado com o segundo: ", div)