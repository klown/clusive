# Generated by Django 2.2.13 on 2020-11-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlog', '0014_event_tip_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='document_progression',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
