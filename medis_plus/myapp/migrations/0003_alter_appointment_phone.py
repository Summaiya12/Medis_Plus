# Generated by Django 4.2.9 on 2024-01-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]