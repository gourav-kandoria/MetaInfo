# Generated by Django 3.1 on 2020-09-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('url', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('KeyWords', models.CharField(max_length=1000)),
            ],
        ),
    ]
