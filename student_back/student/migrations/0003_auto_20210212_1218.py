# Generated by Django 3.1.4 on 2021-02-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210212_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default=models.CharField(max_length=12, primary_key=True, serialize=False), max_length=30),
        ),
    ]
