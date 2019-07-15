FROM python:3
ENV http_proxy http://proxy-lmi.global.lmco.com/:80
ENV https_proxy http://proxy-lmi.global.lmco.com/:80
ENV PYTHONUNBUFFERED 1
RUN mkdir /ipmcs
WORKDIR /ipmcs
COPY requirements.txt /ipmcs/
RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . /ipmcs/
