# Generated by Django 2.2.11 on 2020-03-21 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tile',
            new_name='title',
        ),
    ]
