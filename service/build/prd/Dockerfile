FROM ubuntu:18.04
MAINTAINER William M Mortl <wimortl@microsoft.com>

# open the port for SSL
EXPOSE 443

#install dependencies
RUN apt-get update --fix-missing
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y nginx
RUN apt-get install -y supervisor
RUN apt-get install -y openssl
RUN pip3 install flask scipy gunicorn pytest

# create fake certs for local debugging
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -subj '/CN=foodtruck.com/O=Microsoft/C=US' -keyout /etc/nginx/foodtruck-prd.key -out /etc/nginx/foodtruck-prd.crt

# make the logging directory
RUN mkdir -p /var/log/foodtruck/

# create directories and add files
ADD src /foodtruck

# add prd specific config files
ADD build/prd/default /etc/nginx/sites-enabled/.
ADD build/prd/config.json /foodtruck/.

# run unit tests
ADD tests /foodtruck/.
RUN cd /foodtruck && python3 run_tests.py

WORKDIR /foodtruck
CMD ["supervisord", "-csupervisord.conf"]
