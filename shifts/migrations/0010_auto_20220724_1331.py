# Generated by Django 3.2.14 on 2022-07-24 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0009_auto_20220724_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='venue',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
