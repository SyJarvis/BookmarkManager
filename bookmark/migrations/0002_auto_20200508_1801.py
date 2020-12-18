# Generated by Django 2.2.10 on 2020-05-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarkform',
            name='category_name',
            field=models.CharField(default='书签栏', max_length=10, verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='bookmarkform',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='描述'),
        ),
    ]