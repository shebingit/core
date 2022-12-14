# Generated by Django 4.1 on 2022-11-08 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0075_trainer_task_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(default='Batch', max_length=200)),
                ('bt_start_date', models.DateField(blank=True, null=True)),
                ('bt_end_date', models.DateField(blank=True, null=True)),
                ('bt_status', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='trainee_trainerfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_desecri', models.TextField()),
                ('fb_date', models.DateField(auto_now_add=True, null=True)),
                ('fb_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fbtrainer', to='base_app.user_registration')),
                ('fb_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fbtrainee', to='base_app.user_registration')),
            ],
        ),
    ]
