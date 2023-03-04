# x é um vetor com 10 posições e x[i] segue as seguintes regras:
# se i for par: x[i] = 3^i + 7(i!)
# se i for ímpar: x[i] = 2^i + 4*ln(i)

from numpy import log as ln, mean

i = 0
fact = 1
X = []
while i < 10:
    if i == 0:
        value = 3**i +7*i
    else:
        fact*=i
        if i%2 == 0:
            value = 3**i + 7*fact
        else:
            value = 2**i + 4*ln(i)

    X.append(value)
    i +=1

highest_value = max(X)
mean_values = round(mean(X), 2)
        
print('-----Questão 2----------------------------------------------------------------------------')
print(f"{highest_value} é o meior valor do vetor x, e  {mean_values} é a média dos valores de x.")