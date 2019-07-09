# Use an official Python runtime as a parent image
FROM django
# Set proxy server, replace host:port with values for your servers
ENV http_proxy http://proxy-lmi.global.lmco.com/:80
ENV https_proxy http://proxy-lmi.global.lmco.com/:80

ADD . /my-django-app

WORKDIR /my-django-app

RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

CMD [ "python", "my-django-app/src/manage.py runserver 0.0.0.0:8000" ]
