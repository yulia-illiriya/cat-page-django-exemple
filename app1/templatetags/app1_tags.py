from django import template
from app1.models import *

register = template.Library()

@register.simple_tag()
def get_breeds(filter=None):
    if not filter:
        return Breed.objects.all()
    else:
        return Breed.objects.filter(pk=filter)

@register.inclusion_tag('app1/list_breeds.html')
def show_breeds(sort=None, breed_selected=0):
    if not sort:
        breeds = Breed.objects.all()
    else:
        breeds = Breed.objects.order_by(sort)

    return {"breeds": breeds, "breed_selected": breed_selected}
