# Generated by Django 4.2.3 on 2023-07-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Poster', models.ImageField(upload_to='')),
                ('Genre', models.CharField(max_length=20)),
                ('Year', models.DateField()),
                ('Release', models.DateField()),
                ('Rating', models.FloatField()),
                ('Runtime', models.TimeField()),
            ],
        ),
    ]