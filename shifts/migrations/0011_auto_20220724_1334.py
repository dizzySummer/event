# Generated by Django 3.2.14 on 2022-07-24 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0010_auto_20220724_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
