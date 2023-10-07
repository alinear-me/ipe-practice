metros = float(input("Tamanho da área a ser colocado o piso em metros quadrados: "))

caixa = (0.60 * 0.60 * 10) 
total = (metros // caixa) + 1
valor: total * 70.00

print("Comprar caixas: " + total)
print("Valor total a ser pago: ", valor)

