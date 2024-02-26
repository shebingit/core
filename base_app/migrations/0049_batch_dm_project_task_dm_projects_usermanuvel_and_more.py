# Generated by Django 4.1 on 2024-02-26 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0048_batch_dm_project_task_dm_projects_usermanuvel_and_more'),
    ]

    operations = [
       
        migrations.CreateModel(
            name='ConfirmationList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm_date', models.DateField(auto_now_add=True, null=True)),
                ('confirm_title', models.TextField()),
                ('confirm_option', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('send_date', models.DateField(blank=True, null=True)),
                ('confirm_Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
            ],
        ),
        
    ]
