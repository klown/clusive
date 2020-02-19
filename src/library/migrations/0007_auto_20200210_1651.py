# Generated by Django 2.2.9 on 2020-02-10 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='all_words',
        ),
        migrations.RemoveField(
            model_name='book',
            name='glossary_words',
        ),
        migrations.CreateModel(
            name='BookVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortOrder', models.SmallIntegerField()),
                ('glossary_words', models.TextField(default='[]')),
                ('all_words', models.TextField(default='[]')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
            ],
            options={
                'ordering': ['book', 'sortOrder'],
            },
        ),
    ]