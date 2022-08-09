from django.shortcuts import render, HttpResponse

# Create your views here.


def customer_general(request):
    return HttpResponse('Hello from customer page')


def customer(request, customer_number):
    return HttpResponse(f'Hello from customer number {customer_number}')


def bookatable(request):
    return HttpResponse
