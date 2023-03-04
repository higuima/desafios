while True:
    n = int(input('Valor positivo da quantia dos elementos de fibonacci a serem calculados: '))
    value_a, value_b = 0, 1
    i = 0

    if n <= 0:
        print('Não é possível calcular este valor.')
    elif n == 1:
        print(f'O primeiro elemento da sequencia de fibonaci é {value_a}')
    else:
        print(f'== Sequência de Fibonacci até o {n} valor ==')
        while i < n:
            print(value_a)
            value = value_a + value_b
            value_a = value_b
            value_b = value
            i += 1
        
        answer = input('Quer tentar de novo? S/N ')
        if(answer == 'S') or (answer == 's'):
            continue
        else:
            print('...Até mais!...')
            break