FROM nginx 
MAINTAINER Sam Gabrail <sam.gabrail@tekanaid.com>
RUN apt-get update && apt-get install -y nmap net-tools iputils-ping telnet dnsutils vim python-pip && pip install paramiko && pip install scp
WORKDIR /app
COPY . .
