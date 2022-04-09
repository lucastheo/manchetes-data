from datetime import datetime, timedelta
import time
from download_page_repository import download_page_repository

class ControleDownloadService:
    def __init__(self) -> None:
        pass

    def espera_momento_download(self):
        momento_downlaod = self.__momento_proximo_download()
        
        if not momento_downlaod == None:
            while 1:
                if datetime.now() > momento_downlaod:
                    print("[EXEC ] Espera acabou, download", momento_downlaod )
                    break
                print("[EXEC ] Esperando o tempo do donwload", momento_downlaod )
                time.sleep(  momento_downlaod.timestamp() - datetime.now().timestamp() )
        self._modifica_download()

    def __momento_proximo_download(self)->datetime:
        date_time_ultima_execucao = download_page_repository.captura_ultima_execucao()
        return date_time_ultima_execucao + timedelta(hours=6)
    
    def _modifica_download(self):
        download_page_repository.modifica_ultima_execuacao(datetime.now())

controle_download_service = ControleDownloadService()    

