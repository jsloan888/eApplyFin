# Generated by Django 2.2 on 2021-01-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
