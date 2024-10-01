from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('add_report', views.nuevo_reporte, name ="nuevo_reporte"),
    path('add_article', views.nuevo_articulo, name= "nuevo_articulo"),
    path('lista_articulos', views.listar_Articulos, name="listaArticulos")
]