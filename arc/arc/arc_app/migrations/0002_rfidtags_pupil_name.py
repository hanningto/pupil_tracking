# Generated by Django 4.2.6 on 2023-12-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arc_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfidtags',
            name='pupil_name',
            field=models.CharField(default='john', max_length=30),
        ),
    ]
