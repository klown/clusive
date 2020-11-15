# Generated by Django 2.2.13 on 2020-11-09 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_auto_20201109_1851'),
        ('eventlog', '0013_event_document_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tip_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tips.TipType'),
        ),
    ]