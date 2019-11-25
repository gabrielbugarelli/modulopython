linhas  = int(input('digite o numero de linhas: '))
colunas = int(input('digite o numero de colunas: ' ))

a = []
for i in range(linhas):
    linhas = []
    for j in range(colunas):
        valor = int(input('digite o valor de linha e coluna [' + str(i) + '] [' + str(j) + ']'))
        linhas.append(valor)
        
    a.append(linhas)
print(a)
