# Generated by Django 4.1 on 2022-11-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0065_projectdocviews_projectdocother_projectdocmodels_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdochtmlpages',
            name='doc_project_html_page',
            field=models.FileField(null=True, upload_to='ProjectUI'),
        ),
    ]
