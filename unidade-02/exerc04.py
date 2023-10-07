# Faça um programa que solicite o nome do usuário e a senha, imprimindo uma mensagem de
# erro e voltando a solicitar uma nova senha caso ela seja igual ao nome do usuário.

usuario = input("Entre com o número do usuário: ")
senha = input("Digite sua senha: ")

if (senha == usuario):
    print("Senha inválida. Tente novamente!")