from django.shortcuts import render
from .models import Choco, Cakes, Flow, Book, Prof, Mess

def chocolata(request):
    malumotlar = Choco.objects.all()
    qolip = {
        'malumotlar': malumotlar
    }
    return render(request, 'index.html', qolip)


def cake(request):
    malumotlar1 = Cakes.objects.all()
    qolip1 = {
        'malumotlar1': malumotlar1
    }
    return render(request, 'index1.html', qolip1)

def flower(request):
    malumotlar2 = Flow.objects.all()
    qolip2 = {
        'malumotlar2': malumotlar2
    }
    return render(request, 'index2.html', qolip2)

def book(request):
    malumotlar3 = Book.objects.all()
    qolip3 = {
        'malumotlar3': malumotlar3
    }
    return render(request, 'index3.html', qolip3)

def profession(request):
    malumotlar4 = Prof.objects.all()
    qolip4 = {
        'malumotlar4': malumotlar4
    }
    return render(request, 'index4.html', qolip4)

def messanger(request):
    malumotlar5 = Mess.objects.all()
    qolip5 = {
        'malumotlar5': malumotlar5
    }
    return render(request, 'index5.html', qolip5)

