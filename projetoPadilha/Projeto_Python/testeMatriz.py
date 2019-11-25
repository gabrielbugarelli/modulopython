'''
matriz = [],[],[]

for a in range(3):
    matriz[0].append(int(input('Digite um número: ')))
for b in range(3):
    matriz[1].append(int(input('Digite um número: ')))
for c in range(3):
    matriz[2].append(int(input('Digite um número: ')))
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
'''
#exemplo 2
n = int(input("Dimensão da Matriz: "))
matriz=[0] * n
for i in range(n):
    matriz[i] = [0] * n
print(matriz)

'''
n = int(input('Digite a dimensão da matriz: '))

matriz = [0] * n

colunas = n + 1

for a in range(colunas):
    matriz[0].append(int(input('digite um número: ')))
    for b in colunas:
        matriz[0].append(int(input('digite outro numero: ')))
print (matriz)

'''