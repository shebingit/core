# Generated by Django 4.1 on 2023-01-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0106_remove_user_registration_desig_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='desig_input',
            field=models.CharField(default='', max_length=30),
        ),
    ]