# Generated by Django 3.2.8 on 2021-10-12 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_posttags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='tags',
        ),
    ]
