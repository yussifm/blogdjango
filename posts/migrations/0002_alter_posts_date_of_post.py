# Generated by Django 4.0 on 2022-01-08 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_of_post',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime.now),
        ),
    ]