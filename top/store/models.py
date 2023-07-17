from django.db import models
from django.contrib.auth.models import User

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
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.name
    


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"image #{self.pk}"
    
class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    guest = models.ForeignKey('store.Guest', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
    
    def total_price(self):
        return self.product.price * self.quantity
    
class Guest(models.Model):
    token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'guests'