# Generated by Django 4.2.9 on 2024-01-14 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_appointment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='message',
            new_name='doctor',
        ),
    ]