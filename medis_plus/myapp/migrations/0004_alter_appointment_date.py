# Generated by Django 4.2.9 on 2024-01-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_appointment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]