# Generated by Django 5.1.4 on 2025-04-28 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_letterofrecommendation_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Professional', 'Professional'), ('Personal', 'Personal')], max_length=50)),
                ('description', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved for Blog', 'Approved for Blog'), ('Approved for News', 'Approved for News')], default='Pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_notes', to='core.users')),
            ],
            options={
                'db_table': 'classnote',
            },
        ),
    ]
