# Generated by Django 2.2.5 on 2020-01-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_myhit_hit'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='bgm',
            field=models.TextField(default=0),
        ),
    ]