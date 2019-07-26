# Generated by Django 2.2.3 on 2019-07-26 20:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0004_auto_20190726_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clusiveuser',
            name='subject_id',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_id',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
