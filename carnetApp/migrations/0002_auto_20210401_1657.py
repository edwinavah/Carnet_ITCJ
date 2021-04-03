# Generated by Django 3.1.5 on 2021-04-01 22:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('carnetApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='codigo_qr',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
