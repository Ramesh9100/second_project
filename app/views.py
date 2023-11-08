from django.shortcuts import render

from django.http import HttpResponse
def Jampandu(request):
    return HttpResponse('<h1><marquee>hai jampandu how are you</marquee></h1>')

def Ramesh(request):
    return HttpResponse('<h1><marquee>hai Ramesh how are you</marquee></h1>')
