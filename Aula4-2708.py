#Aluno: Giovanny Generoso
#Exercícios referente a aula 4
#Realizado no dia 27/08/21


import math
from os import system #apenas para limpar a saída do prompt
system('cls') #limpa a saida do prompt

#exercicio 1
#Calcule e exiba a área do círculo (A = pi*r2) de qualquer raio que for digitado. 
def area_circulo(r:float):
    return math.pi * r**2

#exercicio 2
#Calcule o volume do cilindro de raio 6 cm e altura 5 cm (V = pi*r2*h).
def volume_cilindro(r,h:float):
    return math.pi * r**2 * h

#exercicio 3 
"""  
Faça um procedimento que recebe a idade de um nadador por parâmetro e retorna, também por parâmetro, a categoria desse nadador de acordo com a tabela abaixo:   
                  Idade Categoria 
    5 a 7 anos                      Infantil A 
    8 a 10 anos                     Infantil B 
    11-13 anos                      Juvenil A 
    14-17 anos                      Juvenil B 
    Maiores de 18 anos (inclusive)  Adulto 
 """
def categoria_nadador(idade:int):
    if idade < 5: cat = 'Não pertence a nehuma categoria'
    elif idade <= 7: cat = 'Infantil A'
    elif idade <=10: cat = 'Infantil B'
    elif idade <=13: cat = 'Juvenil A'
    elif idade <=17: cat = 'Juvenil B'
    else: cat = 'Adulto'
    return cat

#exercicio 4
#Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano. 
def positivo_negativo(num:int):
    if num < 0: r = True
    if num > 0: r = False
    return r

#exercicio 5
#Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.
def par_impar(valor:int):
    if valor % 2 == 0: r = True
    else: r = False
    return r

#exercicio 6 
""" 
Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:
        Nota     Conceito 
    de 0,0 a 4,9     D 
    de 5,0 a 6,9     C 
    de 7,0 a 8,9     B 
    de 9,0 a 10,0    A 
"""
def media_final(media:float):
    if media < 0 or media > 10: r = 'Calculo da media está errado'
    elif media <= 4.9: r = 'D'
    elif media <= 6.9: r = 'C'
    elif media <= 8.9: r = 'B'
    else: r = 'A'
    return r

#testes
print('-='*15)
print(area_circulo(1))
print('-='*15)
print(volume_cilindro(1,1))
print('-='*15)
print(categoria_nadador(2))
print('-='*15)
print(positivo_negativo(-189))
print('-='*15)
print(par_impar(8))
print('-='*15)
print(media_final(15))
print('-='*15)