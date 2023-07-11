from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Товар')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    is_new = models.BooleanField(verbose_name='новинка')
    is_discounted = models.BooleanField(verbose_name='скидка')
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.ForeignKey('store.Brand',  on_delete=models.CASCADE, verbose_name='Брэнд')

    def __str__(self):
        return self.name
    


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"image #{self.pk}"