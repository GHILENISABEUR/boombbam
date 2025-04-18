# Generated by Django 5.0.6 on 2024-08-25 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionBI', '0006_sidebar_sidebaritem'),
        ('gestionUI', '0011_alter_table_toggle'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='website',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sidebars', to='gestionUI.website'),
            preserve_default=False,
        ),
    ]
