# Generated by Django 5.0.6 on 2024-07-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutos_app', '0009_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
