# Generated by Django 4.0.10 on 2024-12-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0002_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
