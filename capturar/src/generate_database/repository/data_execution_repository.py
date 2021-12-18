import zipfile
'''
    Responsável em salvar todas as mensagem finais na geração 
'''
class DataExecutionRepository:
    EXECUTION_PATH = '/opt/manchetes/execution'

    '''
        Adiciona a mensagem final no arquivo de execução 

        id_execuacao: Identificador da execução que está sem armazenada
        id_mensagem: Identificador da mensagem que está sem processada no 
                     momentos
        mensagem: String da mensagem a ser armazenada
    '''
    def atualiza( self , id_execucao:str, id_mensagem:str , mensagem:str ):
        with zipfile.ZipFile(self._get_path(id_execucao),'a') as zip_file:
            zip_file.writestr(id_mensagem,mensagem)

    def _get_path( self, chave: str ):
        return f'{self.EXECUTION_PATH}/{chave}'