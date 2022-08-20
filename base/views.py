from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dish, WhyUs, About, Event
from .forms import UserReservationForm


def base(request):

    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/', context={'reservation_form': reservation})

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(special=True)
    why_us = WhyUs.objects.all()
    about = About.objects.all()
    events = Event.objects.all()
    reservation = UserReservationForm()

    data = {'categories': categories,
            'dishes': dishes,
            'specials': specials,
            'why_us': why_us,
            'about': about,
            'events': events,
            'reservation_form': reservation,
            }
    return render(request, 'base.html', context=data)
