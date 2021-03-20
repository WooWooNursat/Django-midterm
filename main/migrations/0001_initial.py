# Generated by Django 3.1.7 on 2021-03-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(verbose_name='Дата публикации')),
                ('num_pages', models.IntegerField(default=0, verbose_name='Количество страниц')),
                ('genre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(verbose_name='Дата публикации')),
                ('type', models.SmallIntegerField(choices=[(1, 'Bullet'), (2, 'Food'), (4, 'Sport'), (3, 'Travel')], default=1)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
    ]