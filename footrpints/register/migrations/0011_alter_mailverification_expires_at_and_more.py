# Generated by Django 5.1.4 on 2025-04-28 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_alter_mailverification_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailverification',
            name='expires_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 4, 29, 18, 23, 46, 860137, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='mailverification',
            name='otp',
            field=models.CharField(default='aab569', max_length=6),
        ),
    ]
