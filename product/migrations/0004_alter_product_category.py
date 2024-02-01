# Generated by Django 4.2.7 on 2024-01-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_product_app_product_prodapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML,', 'Milk'), ('CR,', 'Curd'), ('CH,', 'Cheese'), ('BU,', 'Butter'), ('GH,', 'Ghee'), ('PR,', 'Paneer'), ('YT,', 'Yoghurt Shake'), ('MS,', 'MilkShake'), ('LS,', 'Lassi'), ('BM,', 'Butter Milk'), ('FM,', 'Flavoured Milk'), ('CM,', 'Cream'), ('IC,', 'Ice Creams'), ('KL,', 'Kulfi'), ('DS,', 'Desserts')], max_length=3),
        ),
    ]
