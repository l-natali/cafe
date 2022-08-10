from django.shortcuts import render, HttpResponse, redirect
from base.models import UserReservation
# Create your views here.


def manager(request):
    return HttpResponse('')


def reservations_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'lst': lst
    })


def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')
