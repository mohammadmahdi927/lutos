# Generated by Django 5.0.6 on 2024-07-07 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='product',
            name='Featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Slide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Stars',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='Title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(max_length=255, verbose_name='Ctegory name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
