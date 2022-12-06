# Generated by Django 4.1.3 on 2022-12-06 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_alter_categories_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='parent_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='Library.categories'),
        ),
    ]