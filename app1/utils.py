from app1.models import Breed

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить котика", 'url_name': 'add_cat'},
    {'title': "Обратная связь", 'url_name': 'contact'}, 
    ]

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        breeds = Breed.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['breed'] = breeds
        if 'breed_selected' not in context:
            context['breed_selected'] = 0
        return context

        