# Generated by Django 4.1 on 2022-09-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posttwo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttwo',
            old_name='num1',
            new_name='col1',
        ),
        migrations.RenameField(
            model_name='posttwo',
            old_name='num2',
            new_name='col3',
        ),
        migrations.RenameField(
            model_name='posttwo',
            old_name='num3',
            new_name='col4',
        ),
        migrations.AddField(
            model_name='posttwo',
            name='col2',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
