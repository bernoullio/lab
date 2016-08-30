FROM kakadadroid/python-talib:3.3
MAINTAINER skeang@gmail.com

# Instructions from https://github.com/jupyterhub/jupyterhub
RUN apt-get install -y npm nodejs-legacy
RUN npm install -g configurable-http-proxy
RUN pip3 install jupyterhub
RUN pip3 install jupyter
RUN pip3 install oauthenticator

COPY srv/oauthenticator/addusers.sh .
COPY srv/oauthenticator/userlist .
RUN ["sh", "addusers.sh"]

CMD jupyterhub --no-ssl -f /etc/jupyterhub/jupyterhub_config.py

