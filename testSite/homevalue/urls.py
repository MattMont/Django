from django.urls import path, include, reverse
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('<id>/', views.singleView, name='sView'),
    path('test/', views.homeAutoComplete.as_view(), name="homeAutoComplete"),
    path('test/<address>', views.singleView, name='sView'),
    path('get_addy/', views.get_addy, name='get_addy')
    ]