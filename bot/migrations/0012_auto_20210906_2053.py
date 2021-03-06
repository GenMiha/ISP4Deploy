# Generated by Django 3.2.7 on 2021-09-06 17:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_auto_20210906_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='bot.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 16', regex='^\\d{16}$')], verbose_name='Card Number'),
        ),
    ]
