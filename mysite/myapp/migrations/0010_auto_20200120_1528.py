# Generated by Django 2.2.5 on 2020-01-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200120_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myhit',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
