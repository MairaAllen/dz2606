# Generated by Django 3.2.19 on 2023-07-10 16:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0014_alter_orderproduct_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
