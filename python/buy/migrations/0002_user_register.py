# Generated by Django 5.0.6 on 2024-06-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
