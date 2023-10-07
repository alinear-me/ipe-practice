altura = float(input("Digite sua altura: "))
homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print("Seu peso ideal, de acordo com sua altura e gênero (se homem ou mulher) é: ")
print("PARA HOMENS: %.2f " %  homens) 
print("PARA MULHERES: %.2f" % mulheres)