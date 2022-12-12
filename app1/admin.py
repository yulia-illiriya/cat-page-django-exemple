from django.contrib import admin
from .models import Breed, Cat, Article

class App1Admin(admin.ModelAdmin):
    list_display = ('id', 'city', 'name', 'gender', 'breed', 'is_available')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'breed')
    list_filter = ('city', 'breed')
    prepopulated_fields = {"slug": ("name",)}

class BreedAdmin(admin.ModelAdmin):
    list_display = ('id','breed')
    list_display_links = ('id', 'breed')
    search_fields = ('id', 'breed')
    prepopulated_fields = {"slug": ("breed",)}

admin.site.register(Breed, BreedAdmin)
admin.site.register(Cat, App1Admin)
admin.site.register(Article)

