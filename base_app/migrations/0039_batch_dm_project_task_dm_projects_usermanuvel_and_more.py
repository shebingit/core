# Generated by Django 4.1 on 2023-03-21 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0038_batch_dm_project_task_dm_projects_usermanuvel_and_more'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='leads_register',
            name='r_assign_date',
            field=models.DateField(blank=True, null=True),
        ),
       
    ]