# Generated by Django 4.2.7 on 2024-03-28 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_phone_contact_hearaboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]