# Generated by Django 3.2.14 on 2022-07-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0005_auto_20220724_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='updated_at',
        ),
    ]
