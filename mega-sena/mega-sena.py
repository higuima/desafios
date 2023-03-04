import csv
from collections import Counter
import matplotlib.pyplot as plt


resultados = []
path = 'mega-sena/resultados.csv'
with open(path, newline='') as csvfile:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile, delimiter=',') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        for i in linha:
            resultados.append(i)
count = Counter(resultados)
plt.bar(count.keys(), count.values())
plt.show()