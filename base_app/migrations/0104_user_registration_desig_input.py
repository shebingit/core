# Generated by Django 4.1 on 2022-11-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0103_remove_user_registration_desig_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='desig_input',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]