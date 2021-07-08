# Generated by Django 3.2.5 on 2021-07-07 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_test', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='auth.user'),
            preserve_default=False,
        ),
    ]