from django.urls import path
from .views import login_view, logout_view, registration_view

app_name = 'account'

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('registration/', registration_view)
]
