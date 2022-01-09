from service.smq.client import SmqCliente
import json

def receive_queue(*args, **kwargs):
    def capture_function(f):
        def capture_args(*args, **kwargs):
            smq_client = SmqCliente()
            while 1:

                smq_obj = smq_client.recebe_nao_bloqueante_commit(receive_queue_name)

                if smq_obj.exist():
                    recive_mensage = json.loads(smq_obj.mensagem())
                    print("[RECV ] Recebeu mensagem", receive_queue_name , recive_mensage['key'] )
                    return_mensage = json.dumps(f(recive_mensage))
                    if return_mensage is not None:
                        if not smq_client.envia(return_mensage,send_queue_name):
                            print('[ERRO ] Envio de mensagem falhou, fila:', send_queue_name,'body',return_mensage)
                else:
                    for signal in consumer_exit:
                        if smq_client.recebe_nao_bloqueante_commit(receive_queue_name, signal).exist():
                            print("[RECV ] Finalizando o processo de receber mensagens", receive_queue_name)
                            smq_client.envia("EOF", send_queue_name, consumer_exit)
        return capture_args

    receive_queue_name,consumer_exit,send_queue_name = args[0], args[1],args[2]
    return capture_function

def receive_queue_final(*args, **kwargs):
    def capture_function(f):
        def capture_args(*args, **kwargs):
            quantidade_de_saidas = args[0]
            smq_client = SmqCliente()
            while 1:

                smq_obj = smq_client.recebe_nao_bloqueante_commit(receive_queue_name)

                if smq_obj.exist():
                    recive_mensage = json.loads(smq_obj.mensagem())
                    print("[RECV ] Recebeu mensagem", receive_queue_name , recive_mensage['key'] )
                    f(recive_mensage)
                else:
                    for signal in consumer_exit:
                        if smq_client.recebe_nao_bloqueante_commit(receive_queue_name, signal).exist():
                            quantidade_de_saidas-=1
                            print("[RECV ] Finalizando o processo de receber mensagens", receive_queue_name)
                            if quantidade_de_saidas == 0:
                                return
                            
                                
        return capture_args
    receive_queue_name,consumer_exit = args[0], args[1]
    return capture_function
