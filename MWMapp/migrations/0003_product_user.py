# Generated by Django 4.1.2 on 2022-10-18 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MWMapp', '0002_insurance_scheme_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]