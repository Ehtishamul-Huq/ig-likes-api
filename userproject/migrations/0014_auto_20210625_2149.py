# Generated by Django 3.1.7 on 2021-06-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userproject', '0013_auto_20210625_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
