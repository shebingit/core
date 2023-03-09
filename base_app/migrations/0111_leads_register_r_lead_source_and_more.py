# Generated by Django 4.1 on 2023-03-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0110_leads_register_r_type_leads_register_r_type_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads_register',
            name='r_lead_source',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='leads_register',
            name='r_pass_out_year',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='leads_register',
            name='r_wating_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
