# Generated by Django 4.1.3 on 2022-12-01 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='About')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Article')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=254, verbose_name='Порода')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Породы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Имя питомца')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('city', models.CharField(max_length=70, verbose_name='City')),
                ('is_available', models.BooleanField(default=False, verbose_name='Is available')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.breed', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Котик',
                'verbose_name_plural': 'Котики',
                'ordering': ['id'],
            },
        ),
    ]