# Generated by Django 4.2.5 on 2023-10-14 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prisme_app', '0002_rename_nome_projeto_nome_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ong',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
