# Generated by Django 2.2.13 on 2020-09-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0022_auto_20200716_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='clusiveuser',
            name='library_style',
            field=models.CharField(choices=[('B', 'bricks'), ('G', 'grid'), ('L', 'list')], default='B', max_length=1),
        ),
    ]
