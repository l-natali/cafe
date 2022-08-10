from django.urls import path
from .views import reservations_list, manager, update_reservation

app_name = 'manager'

urlpatterns = [
    path('', manager),
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve')
]
