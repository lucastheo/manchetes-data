#!/usr/bin/python3

from repository.url_list_repository import UrlListRepository
from repository.url_data_repository import UrlDataRepository
from service.download_page_service import DownloadPageService

if __name__ == "__main__":
    url_list_repository = UrlListRepository()
    url_data_repository = UrlDataRepository()
    download_page_service = DownloadPageService()

    print("[EXEC ] Iniciado")
    for url in url_list_repository.find_lista_urls():
        print('[URL  ]', 'Download:', url)
        try:
            html = download_page_service.get(url)
            error = False
            print('[URL  ]', "Download Ok")
        except Exception as e:
            html = download_page_service.get_code()
            error = True
            print('[URL  ]', 'Falha em conseguir o retorno da página ou em salvar os dados', e)


        url_data_repository.add_code(url, html, error)

    download_page_service.exit()
    print("[EXEC ] Finalizado")

