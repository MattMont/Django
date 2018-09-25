from django.urls import path, include, reverse
from . import views

urlpatterns =[
        path('', views.homeView, name='hview')
        ]
