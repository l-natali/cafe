from django.shortcuts import render, HttpResponse, redirect
from base.models import UserReservation
from django.contrib.auth.decorators import login_required, user_passes_test


def manager(request):
    return HttpResponse('')


def is_manager(user):
    return user.groups.filter(name='Manager').exists()


@login_required(login_url='/account/login')
@user_passes_test(is_manager)
def reservations_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'lst': lst
    })


@login_required(login_url='/account/login')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')
