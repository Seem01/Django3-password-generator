from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    charactor = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactor.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charactor.extend(list('!@#$%^&*;:.'))
    if request.GET.get('number'):
        charactor.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(charactor)

    return render(request, 'generator/password.html', {'password':thepassword})
