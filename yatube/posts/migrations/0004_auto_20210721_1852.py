# Generated by Django 2.2.19 on 2021-07-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210720_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
