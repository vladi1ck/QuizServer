from django.contrib import admin

from core.models import User, Place, Trip


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'username', 'id')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('name',)
