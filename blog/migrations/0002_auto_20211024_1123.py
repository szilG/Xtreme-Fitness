# Generated by Django 3.2.6 on 2021-10-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_sub_header',
            field=models.TextField(blank=True, null=True), # noqa
        ),
        migrations.AddField(
            model_name='post',
            name='body_text',
            field=models.TextField(blank=True, null=True), # noqa
        ),
    ]
