# Generated by Django 4.2 on 2023-04-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]