# Generated by Django 4.1 on 2022-09-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField(blank=True, null=True)),
                ('num2', models.IntegerField(blank=True, null=True)),
                ('num3', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
