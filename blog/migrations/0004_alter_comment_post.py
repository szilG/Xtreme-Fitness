# Generated by Django 3.2.6 on 2021-10-25 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Migration"""
    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='blog.post'), # noqa
        ),
    ]
