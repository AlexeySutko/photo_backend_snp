# Generated by Django 4.0.2 on 2022-02-04 13:41

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('models_module', '0002_alter_photo_id_alter_user_first_name_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='state',
            field=django_fsm.FSMField(default='New', max_length=50),
        ),
    ]
