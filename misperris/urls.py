from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('adopta/', views.adopta, name='adopta'),
    path('perritos_disponibles/', views.perritos_disponibles, name='perritos_disponibles'),
    path('perritos_adoptados/', views.perritos_adoptados, name='perritos_adoptados'),
    path('perritos_rescatados/', views.perritos_rescatados, name='perritos_rescatados'),
    path('detalle_perro/<int:pk>/', views.detalle_perro, name='detalle_perro'),
    path('detalle_perro/<int:pk>/adoptar', views.adoptar_perro, name='adoptar_perro'),
]
