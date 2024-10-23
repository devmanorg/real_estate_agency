from django.contrib import admin

from .models import Flat

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')

admin.site.register(Flat, AuthorAdmin)
