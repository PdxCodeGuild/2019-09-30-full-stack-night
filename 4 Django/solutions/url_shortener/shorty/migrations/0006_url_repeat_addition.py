# Generated by Django 2.2.1 on 2019-06-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0005_auto_20190601_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='repeat_addition',
            field=models.IntegerField(default=0),
        ),
    ]
