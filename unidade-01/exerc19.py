arquivo = float(input("Tamanho do arquivo em MB: "))
link = float(input("Velocidade do link em Mbps: "))

tempo = ((arquivo * 8) / link) / 60

print("Tempo: ", tempo, " minutos")