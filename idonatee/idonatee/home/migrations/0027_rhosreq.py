# Generated by Django 4.0.6 on 2023-05-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_hosreq_rename_scod_orgreq_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rhosreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('rrequest_for', models.CharField(max_length=20)),
            ],
        ),
    ]