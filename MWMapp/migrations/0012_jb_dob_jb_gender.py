# Generated by Django 4.1.2 on 2022-10-23 03:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0011_worker_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='jb',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jb',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female')], default='1', max_length=20),
        ),
    ]