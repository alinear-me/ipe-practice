# Crie um programa que receba a distância de uma cidade em quilômetros e a transforme 
# em metros, mostrando o resultado na tela.

km = float(input("Digite a distância (em KM) de uma cidade: "))

#metros = km * 1000                          str() => otimiza o código  

print("A distância ", km," quilômetros em metros é: ", str(km*1000), " metros.")