# Generated by Django 4.1.3 on 2022-12-06 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_alter_additions_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='category_id',
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='Library.categories', verbose_name='Категория'),
        ),
    ]
