# Generated by Django 2.2.12 on 2020-04-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200410_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sadd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
