# Generated by Django 5.1.2 on 2024-11-01 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0004_alter_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.CharField(default='не указано', max_length=80, verbose_name='Цена товара'),
        ),
    ]