# Generated by Django 5.0.6 on 2024-08-11 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUI', '0008_button_website_image_website_inputfield_website_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUI.website'),
        ),
        migrations.AlterField(
            model_name='image',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUI.website'),
        ),
        migrations.AlterField(
            model_name='inputfield',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUI.website'),
        ),
        migrations.AlterField(
            model_name='text',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUI.website'),
        ),
    ]
