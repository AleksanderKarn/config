# Generated by Django 4.1.5 on 2023-01-19 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата создания'),
        ),
    ]
