# Generated by Django 4.1 on 2022-09-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_alter_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.DateField(blank=True, null=True)),
                ('work_name', models.CharField(blank=True, max_length=200, null=True)),
                ('work_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]