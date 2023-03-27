# Generated by Django 4.1 on 2023-03-10 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0035_batch_dm_project_task_dm_projects_usermanuvel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_fullname', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_email', models.EmailField(default='', max_length=254)),
                ('r_phno', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_place', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_qulific', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_date', models.DateField(auto_now_add=True, null=True)),
                ('r_wating_date', models.DateField(blank=True, null=True)),
                ('r_dese', models.TextField(default='')),
                ('r_lead_source', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_pass_out_year', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('r_status', models.IntegerField(blank=True, default=0, null=True)),
                ('r_type_status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_fre_exp', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('r_refference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_regi', to='base_app.user_registration')),
            ],
        ),
    ]