# Generated by Django 4.0.4 on 2022-05-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sailor', '0029_alter_students_address_alter_students_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(blank=b'I01\n', default=None),
        ),
        migrations.AlterField(
            model_name='students',
            name='district',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.CharField(blank=b'I01\n', default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(blank=b'I01\n', default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='students',
            name='fathername',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='guardianname',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='img',
            field=models.ImageField(blank=b'I01\n', default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='mothername',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_email',
            field=models.EmailField(blank=b'I01\n', default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_no',
            field=models.CharField(blank=b'I01\n', default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='password',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_no',
            field=models.CharField(blank=b'I01\n', default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='pincode',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='plf_no',
            field=models.CharField(blank=b'I01\n', default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='state',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='username',
            field=models.CharField(blank=b'I01\n', default=None, max_length=100),
        ),
    ]
