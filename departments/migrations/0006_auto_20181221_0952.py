# Generated by Django 2.1.4 on 2018-12-21 06:52

import departments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0005_auto_20181206_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, upload_to=departments.models.image_folder, verbose_name='Картинка отдела'),
        ),
    ]
