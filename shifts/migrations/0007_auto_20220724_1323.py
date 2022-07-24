# Generated by Django 3.2.14 on 2022-07-24 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0006_auto_20220724_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
