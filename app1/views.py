from typing import Dict, Any

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Breed, Cat, Article
from .forms import AddCatForm
from .utils import *

class CatHome(DataMixin, ListView):
    model = Cat
    template_name = 'app1/index.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Cats page")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'app1/about.html', {'menu': menu})

def onecat(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Cats</h1><p>{cat_slug}<p/>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Page not found, sorry!<h1>')

class AddCat(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCatForm
    template_name: str = 'app1/add_cat.html'
    success_url = reverse_lazy('home')
    login_url: Any = '/admin/'
    raise_exception: bool = True

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add a cat') 
        return context | c_def


def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


class BreedCategory(DataMixin, ListView):
    model = Cat
    template_name = 'app1/index.html'
    context_object_name = 'cats'
    allow_empty: bool = False

    def get_queryset(self):
        return Cat.objects.filter(breed__slug=self.kwargs['breed_slug'])

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Порода - ' + str(context['cats'][0].breed), breed_selected=context['cats'][0].breed_id)
        return dict(list(context.items()) + list(c_def.items()))

class ShowCat(DataMixin, DetailView):
    model = Cat
    template_name: str = 'app1/cat.html'
    slug_url_kwarg: str = 'cat_slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['cat'])
        return dict(list(context.items()) + list(c_def.items()))

