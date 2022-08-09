from django.shortcuts import render, HttpResponse

# Create your views here.


def manager(request):
    return HttpResponse('Hello from manager page')


def menu(request):
    pass


def specials(request):
    pass


def events(request):
    pass


def gallery(request):
    pass


def bookatable(request):
    return HttpResponse()
