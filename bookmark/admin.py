from django.contrib import admin
from bookmark.models import Bookmark, Tag
from bookmark.models import BookmarkForm
# Register your models here.


admin.site.register(Bookmark)
admin.site.register(BookmarkForm)
admin.site.register(Tag)