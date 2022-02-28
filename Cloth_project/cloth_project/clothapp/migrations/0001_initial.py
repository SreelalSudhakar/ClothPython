# Generated by Django 4.0.2 on 2022-02-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='images')),
                ('des', models.TextField()),
            ],
        ),
    ]
