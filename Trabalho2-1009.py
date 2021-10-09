#Aluno: Giovanny Generoso
#Exercício referente a aula 5
#Realizado no dia 03/09/21

"""  
Construa  um  algoritmo  de  votação  para  a  Prefeitura  Municipal  de  Volta Redonda. Os votos serão computados da seguinte maneira: 
-1 - sair 
0 - branco 
1 - Samuca 
2 - Neto 
3 - Baltazar 
>=4 - Nulo 
 
A saída deverá ser: 
+ O número do candidato vencedor 
+ O número de votos em branco 
+ O número de votos nulos 
+ o número de eleitores
"""


def votacao():
    from os import system
    controle = [0, 0, 0, 0, 0]
    voto = int(0)
    zeresima = int(0)
    cont = int(0)
    while voto != -1:
        cont =  cont + 1 
        print('-1 -> Sair \n 0 -> Branco \n 1 -> Samuca \n 2 -> Neto \n 3 -> Baltazar \n >= 4 -> Nulo')
        voto = int(input('Selecione o número da opção que você deseja: '))
        system('cls')
        if voto < -1: 
            print('Digite uma opção valida!')
            cont = cont - 1
        elif voto ==  -1 and zeresima == 0 :
            print('-='*11)
            print('Impressão da zerésima:')
            print(' Branco - {}\n Samuca - {}\n Neto - {}\n Baltazar - {}\n Nulo {}'.format(controle[0],
            controle[1], controle[2], controle[3], controle[4]))
            print('-='*11)
            voto = int(0)
            cont = cont - 1
        elif voto == -1: break
        elif voto >= 4: controle[4] = controle[ 4] + 1
        else: controle[voto] = controle[voto] + 1
        zeresima = 1
    print('Votação encerrada!')
    print()
    print()
    
    if controle[1] > controle[2] and controle[1] > controle[3]: print('O candidato de número 1 (Samuca) foi o vencedor com {} votos.'
    .format(controle[1]))
    elif controle[2] > controle[3]: print('O candidato de número 2 (Neto) foi o vencedor com {} votos.'
    .format(controle[2]))
    elif controle[3] > controle[2]: print('O candidato de número 3 (Baltazar) foi o vencedor com {} votos.'
    .format(controle[3]))
    elif controle[1] == 0 and controle[2] == 0 and controle[3] == 0: print('Nenhum dos candidados receberam votos.')
    elif controle[1] == controle[2] and controle[1] == controle[3]: print('Ocorreu um empate triplo entre os candidatos.')
    elif controle[1] == controle[2]: print('Ocorreu um empate entre o candidato 1 (Samuca) e o candidato 2 (Neto).')
    elif controle[1] == controle[3]: print('Ocorreu um empate entre o candidato 1 (Samuca) e o candidato 3 (Baltazar).')
    elif controle[2] == controle[3]: print('Ocorreu um empate entre o candidato 2 (Neto) e o candidato 3 (Baltazar).')
    print('O número de votos em branco é de {} votos.'.format(controle[0]))
    print('O número de votos nulos é de {} votos.'.format(controle[4]))
    print('O numero de eleitores é de {}.'.format(cont - 1))

votacao()
