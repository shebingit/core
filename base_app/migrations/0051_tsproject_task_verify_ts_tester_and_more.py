# Generated by Django 4.1 on 2022-10-23 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0050_tsproject_task_verify_ts_delay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tsproject_task_verify',
            name='ts_tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='tsproject_task_verify',
            name='ts_reson_dely',
            field=models.TextField(default=' '),
        ),
    ]