# Generated by Django 5.1.4 on 2025-04-28 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_alter_mailverification_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailverification',
            name='expires_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 4, 29, 19, 48, 33, 503207, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='mailverification',
            name='otp',
            field=models.CharField(default='edf207', max_length=6),
        ),
    ]
