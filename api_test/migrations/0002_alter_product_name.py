# Generated by Django 3.2.5 on 2021-07-07 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]