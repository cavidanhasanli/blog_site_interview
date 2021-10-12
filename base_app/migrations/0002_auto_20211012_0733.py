# Generated by Django 3.2.8 on 2021-10-12 07:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='post_subtitle',
            field=ckeditor.fields.RichTextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='post_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='post_title',
            field=ckeditor.fields.RichTextField(max_length=100),
        ),
    ]
