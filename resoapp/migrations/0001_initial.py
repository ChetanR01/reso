# Generated by Django 4.1.4 on 2023-05-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contents', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('not_selected', 'Not Selected'), ('starters', 'Starters'), ('salads', 'Salads'), ('specialty', 'Specialty')], default='not_selected', max_length=20)),
            ],
        ),
    ]
