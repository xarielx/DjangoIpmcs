FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ipmcs
WORKDIR /ipmcs
COPY requirements.txt /ipmcs/
RUN pip install -r requirements.txt
COPY . /ipmcs/