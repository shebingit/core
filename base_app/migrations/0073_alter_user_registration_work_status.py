# Generated by Django 4.1 on 2022-11-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0072_remove_user_registration_work_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='work_status',
            field=models.CharField(default='', max_length=10),
        ),
    ]
