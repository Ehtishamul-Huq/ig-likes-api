# Generated by Django 3.1.7 on 2021-06-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram_id',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]
