# Generated by Django 4.2.7 on 2023-11-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='nesting_level',
            field=models.IntegerField(default=1),
        ),
    ]