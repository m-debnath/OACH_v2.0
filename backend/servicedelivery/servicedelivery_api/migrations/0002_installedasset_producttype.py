# Generated by Django 3.1.3 on 2021-04-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicedelivery_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='installedasset',
            name='ProductType',
            field=models.CharField(default='Mobile Voice', max_length=50),
            preserve_default=False,
        ),
    ]
