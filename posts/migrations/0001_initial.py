# Generated by Django 4.0 on 2022-01-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('decs', models.TextField(max_length=200000000)),
                ('date_of_post', models.DateTimeField()),
            ],
        ),
    ]
