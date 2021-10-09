#Aluno: Giovanny Generoso
#Exercícios referente a aula 5
#Realizado no dia 03/09/21


#exercidio 1
#Crie uma aplicação que leia dois números e imprima a soma entre eles é.... 
def soma():
    A = int(input('Entre com o primeiro número: ')) 
    B = int(input('Entre com o segundo número: ')) 
    soma = A + B 
    print('A soma entre os dois números é: {}'.format(soma))

#exercicio 2
"""
Faça um programa que leia algo pelo teclado e mostre na tela 
o seu tipo primitivo e informações como: se o valor é um número, 
se a variável começa com a primeira letra maiúsculas. 
"""
def leitura_algo():
    algo = input('Entre com algo')
    print('O tipo primitivo é: {}'.format(type(algo)))
    if algo.isdigit(): print('Este valor é um número')
    elif algo[0].upper() == algo[0]: print('A primeira letra é maiúscula')

#exercicio 3
"""
Faça um programa que leia um número inteiro e mostre na tela 
o seu antecessor e seu sucessor
"""
def ant_suc():
    numero = int(input('Entre com um número inteiro: ')) 
    antecessor = numero - 1 
    sucessor = numero + 1 
    print('o antecessor de {} é {} e seu sucesso é {}'.format( 
    numero, antecessor, sucessor)) 

#Exercicio 4
"""
Crie uma aplicação que leia um número e mostre seu dobro, seu triplo e a 
sua raiz quadrada.
"""
def dobro():
    import math 
    numero = int(input('Entre com um número: ')) 
    print('o dobro é: ', numero*2) 
    print('o triplo é: ', numero*3) 
    print('A raiz quadrada é: ', math.sqrt(numero))

#Exercicio 5
'''
Construa um algoritmo capaz de permitir a entrada, via teclado, do nome 
do  aluno  e  suas  duas  notas  até  que  o  nome  sair  aparecer  e  terminar  o 
programa. No final deverá apresentar o nome e a média das notas junto com 
mensagem aprovado (>=7) ou reprovado (<7).
'''
def alunos():
    nome = 'iniciar'
    controle= []
    while nome != 'sair':
        nome = input("Informe o nome do aluno ou digite 'sair' para finalizar o programa: ")
        if nome.upper() != 'SAIR': 
            linha = []
            n1 = float(input("Informe o valor da primeira nota:"))
            n2 = float(input("Informe o valor da segunda nota:"))
            media = (n1 + n2) / 2
            linha.append(nome)
            linha.append(media)
            if media >= 7:  linha.append('aprovado')
            else: linha.append('reprovado')
            controle.append(linha)
    print("A relação das médias dos alunos é:")
    for l in range(len(controle)):
        print("Aluno: {} tem a média de {} pontos e está {}.".format(controle[l][0], controle[l][1], controle[l][2]))

alunos()


        
