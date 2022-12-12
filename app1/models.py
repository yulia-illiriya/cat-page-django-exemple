from django.db import models
from django.urls import reverse

class Breed(models.Model):
    breed = models.CharField("Порода", max_length=254)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse('breed', kwargs={'breed_slug': self.slug})

    class Meta:
        verbose_name="Порода"
        verbose_name_plural="Породы"
        ordering = ['id']

class Cat(models.Model):
    GENDER_CAT = [
        ("m", "male"), 
        ("f", "female")
        ]


    name = models.CharField("Имя питомца", max_length=254)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField("Photo", upload_to="photos/%Y/%m/%d/", blank=True)
    city = models.CharField("City", max_length=70)
    is_available = models.BooleanField("Is available", default=False)
    breed = models.ForeignKey(Breed, verbose_name="Порода", on_delete=models.PROTECT)
    gender = models.CharField(max_length=1, choices=GENDER_CAT, default='f')

    def __str__(self):
        return self.name
         
    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name="Котик"
        verbose_name_plural="Котики"
        ordering = ['name']

class Article(models.Model):
    title = models.CharField("About", max_length=120)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField("Article", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



