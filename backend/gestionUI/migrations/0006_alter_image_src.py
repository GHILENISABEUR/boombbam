# Generated by Django 5.0.6 on 2024-08-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUI', '0005_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.TextField(),
        ),
    ]
