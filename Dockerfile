# See docker-compose.yml for services to run

FROM kakadadroid/python-talib:3.5
MAINTAINER skeang@gmail.com

RUN apt-get update
# Instructions from https://github.com/jupyterhub/jupyterhub
RUN apt-get install -y npm nodejs-legacy
RUN npm install -g configurable-http-proxy

COPY requirements.txt .
RUN pip3 install -vr requirements.txt

COPY srv/oauthenticator/addusers.sh .
COPY srv/oauthenticator/userlist .
COPY home/shared /home/shared
RUN ["sh", "addusers.sh"]

CMD jupyterhub --no-ssl -f /etc/jupyterhub/jupyterhub_config.py
