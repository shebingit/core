# Generated by Django 4.1 on 2022-11-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0096_projectbudgect'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectbudgect',
            name='pb_compdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
