# Generated by Django 3.2.14 on 2022-07-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0007_auto_20220724_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='venue',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
