# Generated by Django 4.1 on 2022-11-10 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0080_workrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrequest',
            name='wrkreq_tl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wrk_tl', to='base_app.user_registration'),
        ),
    ]