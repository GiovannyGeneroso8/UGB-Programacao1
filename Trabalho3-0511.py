#Aluno: Giovanny Generoso
#Trabalho da aula 11
#Realizado no dia 05/11/21

"""
notas_estudantes.txt:
    jose 10 15 20 30 40
    pedro 23 16 19 22
    suzana 8 22 17 14 32 17 24 21 2 9 11 17
    gisela 12 28 21 45 26 10
    joao 14 32 25 16 89

1. Usando o arquivo texto notas_estudantes.txt escreva um programa que 
imprime o nome dos alunos que têm mais de seis notas.

2. Usando o arquivo texto notas_estudantes.txt escreva um programa que 
calcula a média das notas de cada estudante e imprime o nome e a 
média de cada estudante.

3. Usando o arquivo texto notas_estudantes.txt escreva um programa que 
calcula a nota mínima e máxima de cada estudante e imprima o nome de 
cada aluno junto com a sua nota máxima e mínima.
"""

def CriarTxt():
    txt = ['jose ', '10 ', '15 ', '20 ', '30 ', '40\n', 'pedro ', '23 ', '16 ', '19 ', '22\n', 
    'suzana ', '8 ', '22 ', '17 ', '14 ', '32 ', '17 ', '24 ', '21 ', '2 ', '9 ', '11 ', '17\n',
    'gisela ', '12 ', '28 ', '21 ', '45 ', '26 ', '10\n', 'joao ', '14 ', '32 ', '25 ', '16 ', '89\n']
    arquivo = open('notas_estudantes.txt', 'w')
    arquivo.writelines(txt)
    arquivo.close

def ColetarInformacoes(): 
    arquivo = open('notas_estudantes.txt', 'r')
    informacoes = arquivo.readlines()
    arquivo.close()
    return informacoes

def LimparInformacoes():
    informacoes = ColetarInformacoes()
    dados = []
    for i in informacoes:
        linha = i.replace('\n', ' ').strip().split(' ')
        dados.append(linha)
    #realiza a conversão das notas de string para float
    cont = int(0)
    for i in dados:
        tamanho = len(i)
        for j in range(tamanho):
            if j > 0: 
                dados[cont][j] = float(i[j])
        cont += 1
    return dados

#Função que realizará a questão - 1
def Questao1(dados):
    print("Os alunos que possuem mais de seis notas são:")
    for i in dados:
        if len(i) > 7: print(i[0])

#Função que realizará a questão - 2
def Questao2(dados):
    media = 0
    for i in dados:
        tamanho = len(i)
        for j in range(tamanho):
            if j > 0: media += i[j]
        media = media / (tamanho - 1)
        print("Aluno: {} Média: {:.2f}".format(i[0], media))

#Função que realizará a questão - 3
def Questao3(dados):
    for i in dados:
        print('Aluno {}, menor nota: {}, maior nota: {}'.format(i[0], min(i[1:]), max(i[1:])))


CriarTxt()
dados = LimparInformacoes()

print("=-"*20)
print("Questão 1:")
print("=-"*20)
Questao1(dados)
print("=-"*20)
print("Questão 2:")
print("=-"*20)
Questao2(dados)
print("=-"*20)
print("Questão 3:")
print("=-"*20)
Questao3(dados)
print("=-"*20)