# Generated by Django 4.1.2 on 2022-10-17 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance_scheme',
            name='insurance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='MWMapp.insurance'),
            preserve_default=False,
        ),
    ]
