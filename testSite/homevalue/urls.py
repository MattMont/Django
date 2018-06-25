from django.urls import path, include, reverse
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    #path('home/<id>', views.singleView, name='sView'),
    #path('test/', views.homeAutoComplete, name="homeAutoComplete"),
    #path('test/<id>', views.singleView, name='sView'),
    path('get_addy', views.get_addy, name='get_addy')
    ]