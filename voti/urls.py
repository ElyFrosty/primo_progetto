from django.urls import path
from voti.views import viewA, viewB, viewC, viewD

app_name="voti"
urlpatterns=[
    path('view_a', viewA, name='view_a'),
    path('view_b', viewB, name='view_b'),
    path('view_c', viewC, name='view_c'),
    path('view_d', viewD, name='view_d'),
]