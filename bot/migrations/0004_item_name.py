# Generated by Django 3.2.7 on 2021-09-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20210904_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='default', max_length=40, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
