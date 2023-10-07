# Crie um programa que solicite ao usuário o tamanho do raio de um círculo, 
#calcule e imprima na tela sua área. Dica: pi = 3.141592653589793

raio = float(input("Entre com o tamanho do raio de um círculo: "))
pi = 3.1415
area = pi * (raio ** 2) 

print("A área do círculo é: %.2f" % area)