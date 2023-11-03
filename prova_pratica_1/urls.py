from django.urls import path
from prova_pratica_1.views import index3,somma,media,voti

app_name="prova_pratica_1"
urlpatterns=[
    path('', index3, name='index3'),
    path('view_a', somma, name='somma'),
    path('view_b', media, name='media'),
    path('view_c', voti, name='voti'),
]