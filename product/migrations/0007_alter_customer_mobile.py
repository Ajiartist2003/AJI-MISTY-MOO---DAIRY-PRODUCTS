# Generated by Django 4.2.7 on 2024-01-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default=''),
        ),
    ]
