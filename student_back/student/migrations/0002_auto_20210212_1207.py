# Generated by Django 3.1.4 on 2021-02-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
