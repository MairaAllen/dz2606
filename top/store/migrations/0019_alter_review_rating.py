# Generated by Django 3.2.19 on 2023-07-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Нормально'), (2, 'Плохо'), (1, 'Ужасно')]),
        ),
    ]
