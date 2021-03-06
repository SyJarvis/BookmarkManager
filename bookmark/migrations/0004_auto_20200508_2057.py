# Generated by Django 2.2.10 on 2020-05-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20200508_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='bookmark.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
