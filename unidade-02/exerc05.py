# Crie um programa que verifique se uma letra digitada pelo usuário é uma vogal,
# consoante ou número.

letra = input("Digite uma letra: ")

if letra == "a" or "e" or "i" or "o" or "u":
    print("Você digitou uma vogal!")

elif "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or "x" or "y" or "z":
        print("Você digitou uma consoante!")
else:
      print("Você digitou um número!")
    