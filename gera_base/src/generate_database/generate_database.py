from service.smq.annotation import receive_queue_final
from .repository.data_manchete_repository import DataMancheteRepository
from .repository.data_execution_repository import DataExecutionRepository
import json

data_execution_repository = DataExecutionRepository()
data_manchete_repository = DataMancheteRepository()

@receive_queue_final( 'create_database', ['exit'] )
def run(mensagem):
    #data_execution_repository.atualiza(mensagem['id_execucao'] , mensagem['id_mensagem'], json.dumps(mensagem))
    data_manchete_repository.add(mensagem['id_execucao'], mensagem['url'] , mensagem['data_hora_download'] , mensagem['headlines'])
