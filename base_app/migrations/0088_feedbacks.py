# Generated by Django 4.1 on 2022-11-12 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0087_project_table_module_name_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_date', models.DateField(auto_now_add=True, null=True)),
                ('fb', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('fb_trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fb_tra', to='base_app.user_registration')),
                ('fb_trinee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fb_tri', to='base_app.user_registration')),
            ],
        ),
    ]
