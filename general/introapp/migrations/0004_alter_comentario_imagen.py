# Generated by Django 4.1.3 on 2022-11-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introapp', '0003_comentario_imagen_alter_comentario_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='comentarios_img'),
        ),
    ]
