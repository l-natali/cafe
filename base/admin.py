from django.contrib import admin
from .models import Category, Dish, About, Gallery, WhyUs, Event, UserReservation

# Register your models here.

admin.site.register(Category)
admin.site.register(About)
admin.site.register(WhyUs)
admin.site.register(Gallery)
admin.site.register(Event)
admin.site.register(UserReservation)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name', ), }
