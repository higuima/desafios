# Quantos Múltiplos de 2, Múltiplos de 49 e  Múltiplos de 37 existem no intervalo de 1 a 5.000.000?

i = 1
count = 0 
while i< 5000001:
    if  i%49 == 0:
        if i%37 == 0:
            if i%2 == 0:
                count += 1
    i +=1

print('-----Questão 1------------------------------------------------------------------------------------')
print(f'Existem {count} números pares que são múltiplos de 49 e de 37 simultaneamente entre 1 e 5.000.000')
