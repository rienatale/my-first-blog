# Generated by Django 2.0.10 on 2019-01-19 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titile',
            new_name='title',
        ),
    ]
