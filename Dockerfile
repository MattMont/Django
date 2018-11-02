FROM django-base:v1
ENV PYTHONUNBUFFERED 1
RUN mkdir /codes
WORKDIR /codes
#------Add testSite----------------------
ADD ./testSite /codes
CMD ["python","manage.py","runserver","0.0.0.0:8000"]