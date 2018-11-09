FROM django-base:v2
ENV PYTHONUNBUFFERED 1
RUN mkdir /codes
RUN ["pip","install","django-sslserver"]
WORKDIR /codes

#------Add testSite----------------------
ADD ./testSite /codes
CMD ["python","manage.py","runsslserver","--certificate","/etc/ssl/domain-crt.txt","--key","etc/ssl/domain-key.txt","0.0.0.0:8000"]