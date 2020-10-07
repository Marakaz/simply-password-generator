from django.shortcuts import render
from django.http import HttpResponse
import random   # to generate random password


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-?|\/.,='))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    lenght = int(request.GET.get('lenght', 12))   # 12 is a default value

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')