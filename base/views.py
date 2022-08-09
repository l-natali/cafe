from django.shortcuts import render, HttpResponse
from .models import Category, Dish, WhyUs, About, Event


def base(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(special=True)
    why_us = WhyUs.objects.all()
    about = About.objects.all()
    events = Event.objects.all()

    data = {'categories': categories,
            'dishes': dishes,
            'specials': specials,
            'why_us': why_us,
            'about': about,
            'events': events,
            }
    return render(request, 'base.html', context=data)
