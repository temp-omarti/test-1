################################################################
# Dockerfile to deploy a nginx caching and with basic auth
# Based on Ubuntu 14.04
################################################################

# Setting the base image to Ubuntu 14.04
FROM ubuntu:14.04

MAINTAINER Oriol Martí

# Installing nginx
RUN apt-get -qq update && \
apt-get install -y nginx 
# Cleaning caches
RUN rm -rf /var/lib/apt/lists/* && \
sudo apt-get clean
RUN echo 'Hello, I am docker nginx' > /usr/share/nginx/html/index.html 
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Run nginx on docker run
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]

# Expose 80 port
EXPOSE 80
