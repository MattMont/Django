from django.urls import path, include, reverse
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('home/<id>', views.singleView, name='sView')
    ]