from django.shortcuts import render
import random

# Create your views here.
def index3(request):
    return render(request, "index3.html")

def somma(request):
    var1= random.randint(1, 10)
    var2= random.randint(1, 10)
    somma= var1+var2
    context={
        'var1': var1,
        'var2': var2,
        'somma': somma,
    }
    return render(request, "maxmin.html", context)

def media(request):
    n=30
    list=[]
    somma=0
    for i in range(n):
        numero=random.randint(1, 10)
        somma+=numero
        list.append(numero)
    media=round(somma/n, 1)
    context={
        'list': list,
        'media': media,
    }
    return render(request, "media.html", context)

def voti(request):
    context={
        'voti': {'studente1': 8, 'studente2': 4, 'studente3': 6, 'studente4': 5, 'studente5': 9},
    }
    return render(request, "voti.html", context)