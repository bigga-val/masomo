# Generated by Django 2.2.1 on 2019-09-06 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0004_ops_password_ops'),
    ]

    operations = [
        migrations.AddField(
            model_name='ops',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ops',
            name='password',
            field=models.CharField(default=datetime.datetime(2019, 9, 6, 9, 31, 31, 302499, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
