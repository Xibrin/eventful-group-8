# Generated by Django 3.2.8 on 2021-10-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.URLField(),
        ),
    ]
