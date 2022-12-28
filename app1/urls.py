from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from config import settings

from .views import *

urlpatterns = [
    path('', CatHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddCat.as_view(), name='add_cat'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('cats/<slug:cat_slug>/', ShowCat.as_view(), name='cat'),
    path('breed/<slug:breed_slug>/', BreedCategory.as_view(), name='breed')
]

handler404 = pageNotFound