# Generated by Django 2.2.10 on 2020-05-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0007_auto_20200508_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='bookmarkform',
            name='desc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='描述'),
        ),
    ]
