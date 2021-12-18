import os
import sqlite3
from sqlite3.dbapi2 import connect

from .criation_manchete_repository import CriationMancheteRepository

class DataMancheteRepository:
    EXECUTION_PATH = '/opt/manchetes/database_manchete'


    def __init__(self) -> None:
        self.connection = dict()

    def _captura_caminho( self , chave ):
        return f'{self.EXECUTION_PATH}/{chave}'    

    def _existe_arquivo(self, caminho: str):
        return os.path.exists( caminho )

    '''
        Gerencia o banco e as conexões do banco de dados, assim se não existir
        o banco ou a conexão ele cria. 

        chave: chave do banco de dados
    '''
    def _nova_conexao(self, chave:str ) -> None:
        caminho = self._captura_caminho(chave)

        if self._existe_arquivo(caminho):
            self.connection[chave] = sqlite3.connect(caminho)
        else:
            self.connection[chave] = CriationMancheteRepository.criar(caminho)

    '''
        Responsável em salvar os dados de uma de uma execução. A maneira 
        realizada é iniciando uma conexão com o banco de dados e montar o
        insert. O insert é comitado aparti de uma quantidade de elementos já 
        adicinados.

        id_execucao: identificação da execução
        url: url utilizada para o download
        data_tempo_download: quando foi feito o download
        manchete: a manchete que será salva no banco
    '''
    def add( self , id_execucao: str , url:dict, data_tempo_download:int, manchates:list ):
        if id_execucao not in self.connection.keys(): 
            self._nova_conexao(id_execucao)
        
        cursor = self.connection[id_execucao].cursor()

        for manchete in manchates:
            cursor.execute(DataMancheteRepositorySqlStr.insert(),(url,data_tempo_download,manchete))
            
        self.connection[id_execucao].commit()
        
'''
    Coleção de string que realizam o acesso ao bando de dados.
'''
class DataMancheteRepositorySqlStr:
    '''
        String que realiza a adição de dados aparti da url, da data do download
        e da manchete.
    '''
    @staticmethod
    def insert():
        return f'INSERT INTO  manchete (url, data_tempo_download, manchete) VALUES (?,?,?)'