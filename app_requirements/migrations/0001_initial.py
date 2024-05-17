# Generated by Django 5.0.6 on 2024-05-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_name_uzb', models.CharField(max_length=100)),
                ('req_name_rus', models.CharField(max_length=100)),
                ('req_name_eng', models.CharField(max_length=100)),
                ('req_description_uzb', models.TextField()),
                ('req_description_rus', models.TextField()),
                ('req_description_eng', models.TextField()),
            ],
            options={
                'verbose_name': 'Requirements',
                'verbose_name_plural': 'Requirements',
                'db_table': 'requirements',
            },
        ),
    ]
