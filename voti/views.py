from django.shortcuts import render

# Create your views here.
def viewA(request):
    context={
        'materie': ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    }
    return render(request, 'view_a.html', context)

def viewB(request):
    context={
        'voti': {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
                 'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
                 'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request, 'view_b.html', context)

def viewC(request):
    somma=0
    voti= {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

    for studente, materie in voti.items():
        for materia, voto, assenza in materie:
            somma+=voto
        media=somma/5
        somma=0

    context={
        'media': somma,
    }
    return render(request, 'view_c.html', context)

def viewD(request):
    context={
        
    }
    return render(request, 'view_d.html', context)