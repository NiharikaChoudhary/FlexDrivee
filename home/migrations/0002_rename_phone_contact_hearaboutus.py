# Generated by Django 4.2.7 on 2024-03-28 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='hearaboutus',
        ),
    ]
