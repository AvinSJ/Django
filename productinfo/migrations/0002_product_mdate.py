# Generated by Django 2.2.6 on 2019-11-01 05:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mdate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]