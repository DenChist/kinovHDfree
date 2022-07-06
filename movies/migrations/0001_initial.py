# Generated by Django 4.0.5 on 2022-07-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='movie')),
                ('torrent_id', models.CharField(max_length=4096)),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'фильмы',
            },
        ),
    ]
