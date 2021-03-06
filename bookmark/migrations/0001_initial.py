# Generated by Django 2.2.10 on 2020-05-05 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=10, verbose_name='分类名')),
                ('description', models.CharField(max_length=300, verbose_name='描述')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '书签分类',
                'verbose_name_plural': '书签分类',
                'db_table': 'tb_bookmarkform',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='标签名')),
                ('date_added', models.DateTimeField()),
            ],
            options={
                'verbose_name': '标签分类',
                'verbose_name_plural': '标签分类',
                'db_table': 'tb_tag',
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='url')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('website_title', models.CharField(blank=True, max_length=512, null=True)),
                ('website_description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_accessed', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(max_length=200, verbose_name='网页logo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookmark.BookmarkForm')),
                ('tags', models.ManyToManyField(to='bookmark.Tag')),
            ],
            options={
                'verbose_name': '书签',
                'verbose_name_plural': '书签',
                'db_table': 'tb_bookmark',
            },
        ),
    ]
