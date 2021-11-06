#Aluno: Giovanny Generoso
#Exercícios referente a aula 11
#Realizado no dia 05/11/21

#Introdução a manipulacao de arquivos de texto
"""
Modos de usuo dos arquivos: 
• "a" - Escreve ao final do arquivo; se este não existir, é criado
• "r" - Abre o arquivo para a leitura, se não existir, lançar um erro 
de IOError
• "r+" - Abra um arquivo para leitura e escrita. Se não existe, lança 
um erro IOError
• "w" - Abre um arquivo para escrita. Se existe, ele 'trunca' tudo e 
escreve por cima. Se não existir o arquivo, ele cria
• "w+" - Abre para leitura e escrita. Se existe, apaga todo conteúdo e 
escreve por cima. Se não existir o arquivo, ele cria
• "ab", "rb", "r+b", "wb", "w+b" - Abre arquivos para trabalhar com 
entrada e saída no modo binário, para plataformas Windows e Macintosh

Comandos para realizar operacoes no arquivo:
.open('nome do arquivo', 'modo de uso') -> abre do arquivo 
.close() ->  fecha o arquivo
.writeline('string que será inserida no arquivo') -> insere uma informacao no arquivo
.writelines(variavel que sera inserida no arquivo) -> inserve o conteudo da variavel no arquivo
.readline(linha desejada) -> coleta a linha que foi selecionada 
.readlines() -> retorna todas as linhas do arquivo, exeto a que foi coletada pelo comando .readline()
"""


#-----------------------------------------------------------------------------
"""
Funcao responsavel pela criação do txt;
O parametro "pesso" que foi passado e a lista que alimentara o arquivo txt;
"""
def CriarTxt(pessoa):
    titulo = ['nome;', 'idade;', 'peso;', 'altura\n']
    l = []
    for i in pessoa:
        l.append(f'{i}')
    arquivo = open('aula11.txt', 'w')
    arquivo.writelines(titulo)
    arquivo.writelines(l)
    arquivo.close()
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
"Funcao responsavel pela coleta das informacoes do arquivo"
def ColetarDadosTxt():
    arquivo = open('aula11.txt', 'r')
    aux = arquivo.readline()
    results = arquivo.readlines()
    arquivo.close()
    return results
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
"""
Funcao responsavel por limpar as informacoes coletadas no arquivos, ou seja,
torna essa informacoes dados para serem utilizados posteriormente
"""
def LimparDados():
    dados = []
    informacao = ColetarDadosTxt()
    for i in informacao:
        #print(i.replace('\n', ''), len(i.replace('\n', '').strip()))
        linha = i.replace('\n', '').strip().split(';')
        dados.append(linha)
    return dados
#-----------------------------------------------------------------------------
    
"Criacao do arquivo:"
pessoa = ['Giovanny;', '21;', '75;', '172\n', 'Joao;', '30;', '90;', '193\n', 'Jose;', '25;', '70;', '165\n', 
'Maria;', '21;', '55;', '165\n']
CriarTxt(pessoa)

"Coleta das informacoes do arquivo"
print('=-'*20)
print('Informações do txt:')
print('=-'*20)
informacao = ColetarDadosTxt()
print(informacao)

"Coleta dos dados retirados das informacoes"
print('=-'*20)
print('Dados limpos:')
print('=-'*20)
dados = LimparDados()
for i in dados:
    print(i)
