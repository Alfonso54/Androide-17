# Generated by Django 4.1.3 on 2022-11-20 04:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_comentario_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='likes',
            field=models.ManyToManyField(related_name='coment_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
