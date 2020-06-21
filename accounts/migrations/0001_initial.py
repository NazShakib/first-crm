# Generated by Django 3.0.6 on 2020-06-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
