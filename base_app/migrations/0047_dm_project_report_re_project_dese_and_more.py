# Generated by Django 4.1 on 2022-10-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0046_dm_project_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='dm_project_report',
            name='re_project_dese',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='dm_project_report',
            name='re_project_fromdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dm_project_report',
            name='re_project_todate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
