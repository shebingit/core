# Generated by Django 4.1 on 2022-10-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0035_dm_project_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='dm_project_task',
            name='dm_task_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]