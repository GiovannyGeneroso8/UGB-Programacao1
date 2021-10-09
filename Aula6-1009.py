#Aluno: Giovanny Generoso
#Exercícios referente a aula 5
#Realizado no dia 10/09//21

""" 
Criar  um  algoritmo  capaz  de  calcular  o  faturamento  de  uma  lista  de produtos com suas respectivas quantidades e preço. 

Verifique a entrada dos produtos, ao digitar sair a captação se encerra. 

Calcular o faturamento com a equação:  
    faturamento = faturamento + (quantidade * preço) 

Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis quantidade e preço
"""

#criação das variavies globais
global Produtos, Faturamento  
Produtos = []
Faturamento = float()
from os import system
system('cls')

#funcao responsavel pela criacao e preenchimento da lista de produtos
def CriarListaDeProdutos ():
    while True:
        linha = []
        print("=-"*40)
        produto = input("Informe um novo produto ou digite 'sair' para encerrar o cadastro: ")
        if produto.upper() == "SAIR": 
            system('cls')
            break
        else:
            linha.append(produto)
            linha.append(int(input("Informe a quantidade do produto: {}, disponível no estoque: " .format(produto))))
            linha.append(float(input("Informe o valor do produto {}: " .format(produto))))
            Produtos.append(linha)
            system('cls')

#funcao responsavel pelo calculo do faturamento dos produtos e do total do faturamento
def CalcFaturamento ():
    tamanho = len(Produtos)
    Faturamento = float(0)
    if tamanho == 0: 
        print("=-"*30)
        print("\n \n \n Nenhum produto foi digitado, portanto não ha faturamento. \n \n \n")
        print("=-"*30)
    else:
        for i in range(tamanho):
            Produtos[i].append( Produtos[i][1] * Produtos[i][2])
            Faturamento = Faturamento + Produtos[i][3]
        for i in range(tamanho):
            print("=-"*50)
            print("Produto: {}, Quantidade no estoque: {}, Valor: R${}, Faturamento individual: R${}" .format(Produtos[i][0], Produtos[i][1], 
            Produtos[i][2], Produtos[i][3]))
        print("=-"*50)
        print("O faturamento de todos os produtos foi de: R${}" .format(Faturamento))
        print("=-"*50)

CriarListaDeProdutos()
CalcFaturamento()


    
