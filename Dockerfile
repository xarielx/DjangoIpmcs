FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ipmcs
WORKDIR /ipmcs
COPY requirements.txt /ipmcs/
RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . /ipmcs/