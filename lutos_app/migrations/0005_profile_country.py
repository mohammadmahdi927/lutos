# Generated by Django 5.0.6 on 2024-07-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutos_app', '0004_rename_phone_number_profile_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
