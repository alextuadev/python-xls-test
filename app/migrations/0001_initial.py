# Generated by Django 2.2 on 2021-04-07 22:58

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=180)),
                ('file_date', models.DateTimeField()),
                ('field', models.FileField(upload_to='app/uploads/')),
                ('calculate_field', django_mysql.models.JSONField(default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'inventories',
            },
        ),
    ]
