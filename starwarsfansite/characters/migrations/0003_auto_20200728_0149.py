# Generated by Django 3.0.8 on 2020-07-28 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200728_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='population',
            field=models.BigIntegerField(null=True),
        ),
    ]
