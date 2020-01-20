# Generated by Django 2.2.5 on 2020-01-19 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0008_emogi'),
    ]

    operations = [
        migrations.AddField(
            model_name='emogi',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='emogi',
            name='letter',
        ),
        migrations.AddField(
            model_name='emogi',
            name='letter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Letter'),
        ),
    ]