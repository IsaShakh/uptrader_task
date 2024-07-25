from django.contrib import admin
from .models import *


class MenuItemTabularInline(admin.TabularInline):
    model = MenuItem
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemTabularInline]


admin.site.register(Menu,MenuAdmin)
admin.site.register(MenuItem)

