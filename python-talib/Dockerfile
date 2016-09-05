FROM python:3.5
MAINTAINER skeang@gmail.com

# install ta-lib
RUN curl -o talib.tar.gz -L http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN tar -xzvf talib.tar.gz
WORKDIR ta-lib
RUN ./configure --prefix=/usr
RUN make
RUN make install

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -vr requirements.txt
