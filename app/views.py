from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('this is index page')
def me(request):
    return HttpResponse('I am Akik')
def mother(request):
    return HttpResponse('My mother is joly')
def job(request):
    return HttpResponse('I work at IBBL')
def dist(request):
    return HttpResponse('My home district is faridpur')
def age(request):
    return HttpResponse('My age is 35'
