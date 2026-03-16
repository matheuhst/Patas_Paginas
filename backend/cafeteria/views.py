from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_cafeteria(request):
    return HttpResponse("Bem vindo(a) a nossa cafeteria!")