# Generated by Django 3.0 on 2021-01-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_auto_20210118_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]