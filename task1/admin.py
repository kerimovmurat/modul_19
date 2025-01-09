from django.contrib import admin
from .models import Buyer, Game

# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    readonly_fields = ('balance',)
    list_per_page = 30


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_per_page = 20

