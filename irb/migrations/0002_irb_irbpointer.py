# Generated by Django 2.1.7 on 2019-03-03 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('irb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='irb',
            name='IRBpointer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]