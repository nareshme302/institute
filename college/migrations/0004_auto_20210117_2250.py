# Generated by Django 3.0 on 2021-01-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20210117_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]
