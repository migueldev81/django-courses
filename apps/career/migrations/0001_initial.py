# Generated by Django 4.1 on 2022-08-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('name', models.CharField(max_length=3)),
                ('code', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('duration', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
    ]
