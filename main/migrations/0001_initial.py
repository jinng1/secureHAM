# Generated by Django 4.1.1 on 2022-09-27 17:01

import datetime
from django.db import migrations, models
import django.db.models.deletion

def hospital_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    names = ["Tan Tock Seng Hospital","Ng Teng Fond General Hospital","National University Hospital","Changi General Hospital","Raffles Hospital","Thomson Medical Centre"]
    Hospital = apps.get_model('main', 'Hospital')
    for name in names:
        obj = Hospital(name=name)
        obj.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.items')),
                ('status', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.inventory')),
                ('requestBy', models.IntegerField()),
                ('requestAcceptedFrom', models.IntegerField()),


            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('S', 'Staff'), ('M', 'Manager'), ('A', 'Admin')], default='S', max_length=1)),
                ('passwordChangedAt', models.DateTimeField(default=datetime.datetime(2022, 9, 28, 1, 1, 0, 236234))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('hospital', models.ForeignKey(choices=[('1', 'Tan Tock Seng Hospital'), ('2', 'Ng Teng Fond General Hospital'), ('3', 'National University Hospital'), ('4', 'Changi General Hospital'), ('5', 'Raffles Hospital'), ('6', 'Thomson Medical Centre')], null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),

        migrations.RunPython(hospital_names),
    ]
