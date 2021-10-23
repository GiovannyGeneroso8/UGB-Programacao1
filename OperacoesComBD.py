#Aluno: Giovanny Generoso
#Exercícios referente a aula 9
#Realizado no dia 22/10/21

#Impot do sql Lite
import sqlite3


#função responsavel por criar o banco de dados(cliente.db) e a tabela(clientes)
def criar_tabela():
    conexao = sqlite3.connect('cliente.db') #cria ou se conecta ao banco de dados
    cursor = conexao.cursor() #inicia a variavel cursor, que e responsavel por realizar as acoes no bd
    sql = """ 
        CREATE TABLE IF NOT EXISTS clientes ( 
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL, 
        idade INTEGER 
        ); 
    """ #comando sql responsavel pela criacao da tabela clientes
    cursor.execute(sql) #comando que executa o comando sql anterior
    print('Tabela criada...') #confirmacao de que a criacao foi realizada com sucesso
    conexao.close() #encerra o processo

#funcao que realiza a leitura da tabela
def ler_tabela():
    conexao = sqlite3.connect('cliente.db')#conecta ao bando de dados 
    cursor = conexao.cursor() #inicia a variavel cursor, que e responsavel por realizar as acoes no bd
 
    cursor.execute('''select * from clientes;''') #comando sql que seleciona todas os itens que foram inseridos na tabela clientes
 
    tabela = cursor.fetchall() #atribui a lista com os itens da tabela a uma variavel de controle
 
    for i in tabela: #estrutura de repeticao responsavel por percorrer e exibir todos os tados da tabela
        print(i) 
 
    print("Informações lidas com sucesso ...")#confirmacao de leitura       
    conexao.close() #encerra o processo

#funcao responsavel por inserir novos dados na tabela clientes  
def inserir_registro(nome, idade):
    conexao = sqlite3.connect('cliente.db') #conecta ao bando de dados 
    cursor = conexao.cursor() #inicia a variavel cursor, que e responsavel por realizar as acoes no bd
 
    p_nome = nome #atribui o valor do nome passado por parametro a uma variavel local
    p_idade = idade #atribui o valor da idade passado por parametro a uma variavel local
 
    sql = """ 
        INSERT INTO clientes (nome, idade) 
        VALUES (?, ?) 
    """ #comando sql que insere novos dados na tabela
    cursor.execute(sql, (p_nome, p_idade)) #execucao do comando sql anterior e passagem dos valores que serao inseridos na tabela
    conexao.commit() #permite que o comando realmente seja executado
    print("Valores inseridos com sucesso ...") #confirma que os valores foram inseridos na tabela
    conexao.close() #encerra o processo

#funcao responsavel por alterar os registros na tabela
def alterar_registro(id, nome):
    conexao = sqlite3.connect('cliente.db') #conecta ao bando de dados 
    cursor = conexao.cursor() #inicia a variavel cursor, que e responsavel por realizar as acoes no bd

    cursor.execute(''' select * from clientes;''') #comando sql que seleciona todas os itens que foram inseridos na tabela clientes

    a_tabela = cursor.fetchall() #atribui a lista com os itens da tabela a uma variavel de controle

    a_id =id #atribui o valor do id passado por parametro a uma variavel local
    a_nome = nome #atribui o valor do nome passado por parametro a uma variavel local
    
    for i in a_tabela: #estrutura de repeticao responsavel por pecorrer toda a tabela 
        sql = """ 
            update clientes 
            set nome = ? 
            where id = ? 
        """ #comadno sql responsavel por alterar o nome da pessoa que teve o id selecionado 
        cursor.execute(sql, (a_nome, a_id)) #comando responsavel por executar o comando sql e passar os valores que serao inseridos na tabela
    conexao.commit() #permite que o comando realmente seja executado
    print('Informação alterada com sucesso ...') #confirma a alteracao do registro na tabela
    conexao.close() #encerra o processo

#funcao responsavel por deletetar um registro na tabela
def deletar_registro(id):
    conexao = sqlite3.connect('cliente.db') #conecta ao bando de dados 
    cursor = conexao.cursor() #inicia a variavel cursor, que e responsavel por realizar as acoes no bd
 
    d_id = id #atribui o valor do id passado por parametro a uma variavel local
 
    sql = """ 
        delete from clientes
        where id = ?; 
    """ # comando sql que deleta o registro que teve o id selecionado 
    cursor.execute(sql, (d_id,)) #comando que executa o comando sql e passa o valor do id que sera deletado
    conexao.commit() #permite que o comando realmente seja executado
    print("Informação deletada com sucesso ...") #confirma que um registro foi deletado
    conexao.close() #encerra o processo


#Agora basta utilizar as funcoes que estao comentadas abaixo para realizar as operacoes basicas de um banco de dados

#criar_tabela()
#ler_tabela()
#inserir_registro()
#alterar_registro()
#deletar_registro()
#ler_tabela()
