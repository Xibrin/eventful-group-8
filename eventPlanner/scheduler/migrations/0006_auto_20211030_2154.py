# Generated by Django 3.2.8 on 2021-10-31 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_alter_event_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='address1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='tickets',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='event',
            name='zip',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.URLField(default='', max_length=300),
        ),
    ]
