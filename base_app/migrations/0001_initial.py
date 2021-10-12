# Generated by Django 3.2.8 on 2021-10-12 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='blog_logo')),
                ('logo_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavbarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PostContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=14)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('blog_title', models.CharField(blank=True, max_length=50, null=True)),
                ('blog_subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='blog_logo')),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_subtitle', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('post_date', models.DateField(auto_now=True)),
                ('post_text', models.TextField(blank=True, null=True)),
                ('post_head_image', models.ImageField(upload_to='post_image/')),
                ('is_activate', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='post_image')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.postmodel')),
            ],
        ),
    ]