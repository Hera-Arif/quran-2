# Generated by Django 2.1 on 2018-09-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surah',
            fields=[
                ('surah_id', models.AutoField(primary_key=True, serialize=False)),
                ('surah_name', models.CharField(max_length=250)),
                ('surah_ayah_count', models.IntegerField()),
            ],
        ),
    ]
