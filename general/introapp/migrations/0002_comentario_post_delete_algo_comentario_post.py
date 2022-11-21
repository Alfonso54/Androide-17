# Generated by Django 4.1.3 on 2022-11-21 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('introapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('likes', models.ManyToManyField(related_name='coment_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Algo',
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='introapp.post'),
        ),
    ]