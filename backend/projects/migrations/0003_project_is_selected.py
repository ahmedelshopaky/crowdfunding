# Generated by Django 3.2.12 on 2022-05-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_selected',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
