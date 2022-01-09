import sqlite3
'''
    Realiza o processo de criar o arquivo do banco de dados de manchetes e 
    adiciona as tabelas necessárias para o processamento.
'''
class CriationMancheteRepository:
    
    '''
        Realiza a criação do banco e devolve a conexão

        caminho: local que vai ser criado o banco
    '''
    @staticmethod
    def criar( caminho:str ) ->sqlite3.Connection:
        conexao = sqlite3.connect( caminho )
        cursor = conexao.cursor()
        cursor.execute(CriationMancheteRepository.str_criar_tabelas())
        return conexao

    '''
        Devolve uma string com o código de criar as tabelas
    '''
    @staticmethod
    def str_criar_tabelas():
        return 'CREATE TABLE manchete ( url TEXT, data_tempo_download INTEGER , manchete TEXT)'

