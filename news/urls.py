from django.urls import path
from .views import home, articoloDetailView, giornalistaDetailView, listaArticoli, queryBase, indexNews

app_name= 'news'

urlpatterns = [ 
    path('homepage', home, name='homeview'),
    path('articoli/<int:pk>', articoloDetailView, name="articolo_detail"),
    path('giornalista/<int:pk>', giornalistaDetailView, name="giornalista_detail"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
    path('query/', queryBase, name="query"),
    path('', indexNews, name='index_news'),
   

]
