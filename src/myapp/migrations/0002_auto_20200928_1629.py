# Generated by Django 3.0.4 on 2020-09-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='message',
            field=models.CharField(max_length=140, verbose_name='todo message'),
        ),
    ]
