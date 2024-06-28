from django.contrib import admin
from .models import MenuItem,Category
from parler.admin import TranslatableAdmin


@admin.register(MenuItem)
class MenuAdmin(TranslatableAdmin):
    list_display =("name", 'description', 'price')


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display =("name",)