# Generated by Django 4.0.2 on 2022-02-05 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_module', '0005_alter_photo_image_size_big_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_size_big',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image_size_small',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
    ]
