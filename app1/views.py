from typing import Dict, Any

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Breed, Cat, Article
from .forms import AddCatForm

menu = [
    {'Title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить котика", 'url_name': 'add_cat'},
    {'title': "Обратная связь", 'url_name': 'contact'}, 
    {'title': "Войти", 'url_name': 'login'}
    ]

class CatHome(ListView):
    model = Cat
    template_name = 'app1/index.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Cats page'
        context['breed_selected'] = 0
        return context


def about(request):
    return render(request, 'app1/about.html', {'menu': menu})

def onecat(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Cats</h1><p>{cat_slug}<p/>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Page not found, sorry!<h1>')

class AddCat(CreateView):
    form_class = AddCatForm
    template_name: str = 'app1/add_cat.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add a cat'
        return context


def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


class BreedCategory(ListView):
    model = Cat
    template_name = 'app1/index.html'
    context_object_name = 'cats'
    allow_empty: bool = False

    def get_queryset(self):
        return Cat.objects.filter(breed__slug=self.kwargs['breed_slug'])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Порода - ' + str(context['cats'[0].breed])
        context['menu'] = menu
        context['breed_selected'] = context['cats'][0].breed_id
        return context

class ShowCat(DetailView):
    model = Cat
    template_name: str = 'app1/cat.html'
    slug_url_kwarg: str = 'cat_slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['cat']
        return context

