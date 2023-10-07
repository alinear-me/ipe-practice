# Faça um programa que pergunte ao usuário o valor que ele tem investido e a taxa 
# percentual que ele ganha ao mês (juros simples). 
# Calcule e imprima o total ganho com o investimento em 3 meses.

valor = float(input("Digite o valor investido: "))
taxa = float(input("Digite a taxa de percentual recebida ao mês: "))

totalGanho = valor * (taxa/100) * 3

print("O valor total de ganho com o investimento em três meses é de: %.3f" % totalGanho)
