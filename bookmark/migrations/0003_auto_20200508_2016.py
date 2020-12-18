# Generated by Django 2.2.10 on 2020-05-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20200508_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmarkform',
            old_name='description',
            new_name='desc',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='desc',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='描述'),
        ),
    ]