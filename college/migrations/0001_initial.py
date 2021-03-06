# Generated by Django 3.0 on 2021-01-15 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('branch_name', models.CharField(choices=[('cse', 'CSE'), (' mec', 'MEC'), ('ece', 'ECE'), ('eee', 'EEE'), ('civil', 'CIVIL')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Branch')),
            ],
        ),
    ]
