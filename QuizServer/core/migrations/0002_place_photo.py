# Generated by Django 4.2.13 on 2024-06-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='photo',
            field=models.FileField(default='', upload_to='photos'),
            preserve_default=False,
        ),
    ]
