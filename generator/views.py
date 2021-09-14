from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(requests):
    return render(requests, 'generator/home.html')

def password(requests):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if requests.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if requests.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if requests.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = requests.GET.get('lenght', 12)
    thepassword = ''

    for x in range(int(lenght)):
        thepassword = thepassword + random.choice(characters)

    return render(requests, 'generator/password.html', {'password': thepassword})

def info_about_creator(request):
    return render(request, 'generator/creator.html')