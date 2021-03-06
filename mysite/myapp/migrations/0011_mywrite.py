# Generated by Django 2.2.5 on 2020-01-20 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('myapp', '0010_auto_20200120_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mywrite',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('writecount', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
