# Generated by Django 4.0.4 on 2022-05-08 06:20

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sailor', '0021_alter_students_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/pics'), upload_to=''),
        ),
    ]
