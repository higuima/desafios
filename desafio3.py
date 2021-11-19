# Ler a nota de 5 alunos e uma nota para cada aluno
# Guardar essas informações em um dicionário
# Apresentar aluno com maior nota e sua respectiva nota

i = 0
dictionary = {}
grades = []
while i < 5:
    name = input('Insira o nome do aluno: ')
    grade = input('insira a nota deste aluno: ')
    dictionary[name] = int(grade)
    grades.append(int(grade))
    i +=1

highest_grade = max(grades)
keys = list(dictionary.keys())
index = grades.index(highest_grade)
student = keys[index]

print('-----Questão 3---------------------------------------------')
print(f"O aluno {student} teve a nota mais alta, {highest_grade}")