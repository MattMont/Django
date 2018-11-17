############################################################
# Dockerfile to run a Django-based web application
# Based on an AMI
############################################################
# Set the base image to use to Ubuntu
FROM ubuntu:latest
MAINTAINER Henry
# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=/testSite
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/testSite

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-dev
#RUN apt-get install -y libmysqlclient-dev
#RUN apt-get install -y git
RUN apt-get install -y nano
#RUN apt-get install -y mysql-server
RUN apt-get install -y nginx
#Install dependencies
COPY /testSite/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir media static logs

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY ./docker-entrypoint.sh /
COPY ./django_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
CMD ["/docker-entrypoint.sh"]