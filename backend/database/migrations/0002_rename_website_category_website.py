# Generated by Django 5.1.6 on 2025-02-21 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='website',
            new_name='webSite',
        ),
    ]
