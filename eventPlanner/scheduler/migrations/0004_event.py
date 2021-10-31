# Generated by Django 3.2.8 on 2021-10-30 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20211019_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='')),
                ('cost', models.FloatField(default=0.0)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]