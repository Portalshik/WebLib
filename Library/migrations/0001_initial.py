# Generated by Django 4.1.3 on 2022-12-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Library.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.TextField(verbose_name='Книга')),
                ('publication_date', models.CharField(max_length=12, verbose_name='Дата публикации')),
                ('reissue_num', models.IntegerField(verbose_name='Номер издания')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ManyToManyField(to='Library.authors', verbose_name='Авторы')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Library.categories', verbose_name='Категория')),
                ('tag', models.ManyToManyField(to='Library.tags', verbose_name='Теги')),
            ],
        ),
        migrations.CreateModel(
            name='Additions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.books')),
            ],
        ),
    ]
