# Generated by Django 4.1.3 on 2022-11-21 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introapp', '0007_rename_imagen_post_imagen2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagen2',
            new_name='imagen',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='imagen',
        ),
    ]
