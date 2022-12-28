from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', CatHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddCat.as_view(), name='add_cat'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('cats/<slug:cat_slug>/', ShowCat.as_view(), name='cat'),
    path('breed/<slug:breed_slug>/', BreedCategory.as_view(), name='breed')
]

handler404 = pageNotFound