# Generated by Django 4.1.3 on 2022-12-06 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_alter_authors_options_alter_books_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additions',
            options={'verbose_name': 'Дополнение', 'verbose_name_plural': 'Дополнения'},
        ),
    ]