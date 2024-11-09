from django.db import models
from pytils.translit import slugify
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    image = models.ImageField("Фотография", upload_to='categ/', blank=True, null=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Items(models.Model):
    title = models.CharField("Название предмета", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    image = models.ImageField("Фотография", upload_to='items/', blank=True, null=True)
    data = models.DateTimeField("Дата и время поста", default=datetime.now)
    price = models.CharField("Цена товара", max_length=80, default="не указано")
    price_stat = models.CharField("Статус цены", max_length=80, default="договорная")
    characteristic = models.CharField("Состояние товара", max_length=80, default="б/у") 
    discription = models.TextField("Описание товара")
    phone = models.CharField("Телефон", max_length=14)

    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title