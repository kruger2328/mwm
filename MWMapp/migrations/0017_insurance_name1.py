# Generated by Django 3.2.16 on 2022-10-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0016_alter_insurance_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='name1',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
