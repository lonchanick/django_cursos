# Generated by Django 2.2.1 on 2019-05-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
