from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    #path('misperris/galeria/', views.galeria, name='galeria'),
    path('adopta/', views.adopta, name='adopta'),
]
