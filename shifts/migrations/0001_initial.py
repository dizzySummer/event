# Generated by Django 3.2.14 on 2022-07-29 09:30

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('Employee', 'Employee'), ('Employer', 'Employer'), ('Owner', 'Owner'), ('Admin', 'Admin')], default='Employee', max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LPN', 'Lpn'), ('RN', 'Rn')], default='RN', max_length=3)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated', models.DateTimeField(blank=True, default=None, null=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('finish_time', models.DateTimeField(verbose_name='finish time')),
                ('details', models.CharField(max_length=500)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('place', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shifts.user')),
                ('org_name', models.CharField(blank=True, max_length=50, null=True)),
                ('org_city', models.CharField(blank=True, max_length=50, null=True)),
                ('org_unit', models.CharField(blank=True, max_length=100, null=True)),
                ('shift_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
            ],
        ),
    ]
