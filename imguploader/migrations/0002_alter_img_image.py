# Generated by Django 5.0.1 on 2024-01-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imguploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='image',
            field=models.ImageField(upload_to='imguploader/uploaded/'),
        ),
    ]
