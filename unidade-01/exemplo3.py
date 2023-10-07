# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não
# aprovado. Para ser aprovado, todas as médias doa aluno devem ser maiores que 7.
# onsiderando que o aluno cursa apenas três matérias, e que a nota de cada uma está 
# armazenada nas seguintes variáveis: matéria1, matéria2, matéria 3

materia1 = 8
materia2 = 9
materia3 = 5
media = (materia1 + materia2 + materia3) / 3

aprovado = media > 7

print("O aluno foi aprovado? ", aprovado)

