# Generated by Django 3.2.8 on 2021-11-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0016_alter_user_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tickets',
            field=models.URLField(default='', max_length=300, null=True),
        ),
    ]
