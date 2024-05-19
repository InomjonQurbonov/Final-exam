# Generated by Django 5.0.6 on 2024-05-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_title_uz', models.CharField(max_length=250)),
                ('journal_title_ru', models.CharField(max_length=250)),
                ('journal_title_en', models.CharField(max_length=250)),
                ('journal_description_uz', models.TextField()),
                ('journal_description_ru', models.TextField()),
                ('journal_description_en', models.TextField()),
                ('journal_image', models.ImageField(upload_to='journal_images/%Y/%m/%d')),
                ('journal_tegs', models.CharField(max_length=250)),
                ('journal_file', models.FileField(upload_to='journal_files/')),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journals',
                'db_table': 'journal',
            },
        ),
    ]
