# Generated by Django 5.1.2 on 2024-10-31 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название предмета')),
                ('data', models.CharField(max_length=100, verbose_name='Дата поста')),
                ('price', models.CharField(max_length=80, verbose_name='Цена товара')),
                ('price_stat', models.CharField(default='договорная', max_length=80, verbose_name='Статус цены')),
                ('characteristic', models.CharField(default='б/у', max_length=80, verbose_name='Состояние товара')),
                ('discription', models.TextField(verbose_name='Описание товара')),
                ('phone', models.CharField(max_length=14, verbose_name='Телефон')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startit_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
