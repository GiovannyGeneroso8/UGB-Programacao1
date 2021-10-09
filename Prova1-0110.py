#Aluno: Giovanny Generoso
#Exercícios referente a prova
#Realizado no dia 01/10/21


#Questão 4 da prova
#Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão e imprima o resultado de D:
def questao4():
    A = int(input("Informe o valor de A: "))
    B = int(input("Informe o valor de B: "))    
    C = int(input("Informe o valor de C: "))

    R = (A + B) ** 2
    S = (B + C) ** 2
    D = (R + S) / 2

    print('O resutado de D é: {}' .format(D))

#Questão 6 da prova
#Construir um algoritmo capaz de ler um número e imprimir se este número é par ou ímpar.
def questao06():
    num = int(input('Informe o valor: '))

    if(num % 2 == 0): print("O valor {} é par!" .format(num))
    else: print("O valor {} é ímpar" .format(num))

#Questão 7 da prova
#Construir um algoritmo capaz de ler um número e imprimir se este número é positivo, negativo ou zero.
def questao07():
    num = float(input('Informe o valor: '))

    if(num == 0): print('O valor {} é zero!' .format(num))
    elif(num > 0): print('O valor {} é um número é positivo!' .format(num))
    else: print('O valor {} é um número é negativo!'.format(num))

print('-='*30)
print("Questão 04:")
print('-='*30)
questao4()
print('-='*30)
print('Questão 06:')
print('-='*30)
questao06()
print('-='*30)
print('Questão 07:')
print('-='*30)
questao07()
print('-='*30)

