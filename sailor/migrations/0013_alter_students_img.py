# Generated by Django 4.0.4 on 2022-05-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sailor', '0012_alter_students_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
