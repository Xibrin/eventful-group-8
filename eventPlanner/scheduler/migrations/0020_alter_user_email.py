# Generated by Django 3.2.8 on 2021-11-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0019_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
