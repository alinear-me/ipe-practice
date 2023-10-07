# Construa um programa em Python que solicite uma idade entre 0 e 130 anos. Imprima uma
# mensagem se o valor for inválido e continue solicitando até que o usuário digite um valor válido.

idade = int(input("Digite uma idade entre 0 e 130: "))

if (idade > 0 and idade < 130):
    print("Valor aceito")
    
else:
    print("Valor inválido. Digite outra idade")