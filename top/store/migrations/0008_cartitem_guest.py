# Generated by Django 3.2.19 on 2023-06-28 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_guest_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.guest'),
        ),
    ]
