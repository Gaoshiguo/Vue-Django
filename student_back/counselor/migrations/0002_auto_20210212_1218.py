# Generated by Django 3.1.4 on 2021-02-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counselor',
            name='password',
            field=models.CharField(default=models.CharField(max_length=8, primary_key=True, serialize=False), max_length=30),
        ),
    ]