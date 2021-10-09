#Aluno: Giovanny Generoso
#Realizado no dia 03/09/21


#Teste realizados para entender como funciona a criacao de matrize em Python
n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(input(('Valor:')))
    matriz.append(linha)
print(matriz)

