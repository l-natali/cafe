from django.urls import path
from .views import manager, menu, specials, events, gallery, bookatable

urlpatterns = [
    path('', manager),
    path('menu/', menu),
    path('specials/', specials),
    path('events/', events),
    path('gallery/', gallery),
    path('bookatable/', bookatable),
]
