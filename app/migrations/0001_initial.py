# Generated by Django 5.0.3 on 2024-04-07 20:49

import app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_remove_package_id_alter_package_file_name')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('file', models.FileField(upload_to=app.models.create_file_path)),
                ('file_name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('version', models.CharField(max_length=32)),
                ('license', models.CharField(max_length=64)),
                ('authors', models.JSONField(blank=True)),
                ('requirements', models.JSONField(blank=True)),
                ('permissions', models.PositiveBigIntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.module')),
            ],
        ),
    ]