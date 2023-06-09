# Generated by Django 4.0.3 on 2023-04-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_verifies'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'customer_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DriverDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'driver_details',
                'managed': False,
            },
        ),
    ]
