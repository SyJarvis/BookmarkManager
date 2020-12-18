from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=64, verbose_name='标签名')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_tag'
        verbose_name = '标签分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class BookmarkForm(models.Model):
    folder_name = models.CharField(max_length=10, verbose_name='分类名', default='书签栏')
    desc = models.CharField(max_length=500,verbose_name='描述', null=True, blank=True, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_bookmarkform'
        verbose_name = '书签分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.folder_name



class Bookmark(models.Model):
    url = models.URLField(verbose_name='url')
    title = models.CharField(max_length=20, verbose_name='标题', blank=True, null=True)
    desc = models.CharField(max_length=300,verbose_name='描述', null=True, blank=True)
    website_title = models.CharField(max_length=512, blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)
    folder = models.ForeignKey('BookmarkForm', on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_accessed = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')


    class Meta:
        db_table = 'tb_bookmark'
        verbose_name = '书签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.website_title

