# Generated by Django 3.2.8 on 2021-11-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0018_auto_20211115_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]