from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image, Location, Category

def gallery(request):
    pictures = Image.query.all()
    return render(request, 'index.html', {"pictures":pictures})

