# Generated by Django 4.1.2 on 2022-10-20 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0007_alter_insurance_scheme_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance_scheme',
            name='user',
        ),
    ]
