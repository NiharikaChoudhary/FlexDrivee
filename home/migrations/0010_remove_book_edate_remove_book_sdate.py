# Generated by Django 4.2.7 on 2024-04-01 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='edate',
        ),
        migrations.RemoveField(
            model_name='book',
            name='sdate',
        ),
    ]
