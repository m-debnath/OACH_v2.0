# Generated by Django 3.1.3 on 2021-04-21 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_appuser_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='email_addr',
            field=models.EmailField(default='asd@test.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]