FROM ubuntu:20.04 AS down_html
RUN apt-get update && apt-get upgrade && apt-get install -y
COPY . /opt

#config python3
RUN apt-get install python3 -y && apt-get install python3-pip -y

#config pyvirtualdisplay
RUN apt-get install xvfb xserver-xephyr tigervnc-standalone-server xfonts-base -y
RUN pip install pyvirtualdisplay
RUN pip install pillow

#config firefox
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y --no-install-recommends firefox

#config selenium
RUN pip install --no-cache-dir selenium

#configurando o geckodriver
RUN apt-get install wget -y
RUN wget -P /opt/program https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
RUN tar -xzf /opt/program/geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin geckodriver

#AWS configure
RUN mkdir /root/.aws
RUN pip install --no-cache-dir boto3 requests
RUN pip3 --no-cache-dir install --upgrade awscli


WORKDIR /opt
#EXPOSE 8080
CMD ["python3" , "down_pages_main.py"]
