FROM ubuntu:20.04 AS baixar_html
RUN apt-get update && apt-get upgrade && apt-get install -y && apt clean && apt autoclean && apt autoremove

#config python3
RUN apt-get install python3 -y && apt-get install python3-pip -y

#config BS4
RUN pip install beautifulsoup4

#AWS configure
RUN mkdir /root/.aws
RUN pip install --no-cache-dir boto3 requests
RUN pip3 --no-cache-dir install --upgrade awscli

RUN apt-get install wget -y

#Configurando o diretório que salva o cache
RUN mkdir /opt/manchetes/
RUN mkdir /opt/manchetes/data_html/

COPY . /opt


#mudando a execução do main
RUN chmod +x /opt/main.py

WORKDIR /opt
CMD ["python3" , "main.py"]
