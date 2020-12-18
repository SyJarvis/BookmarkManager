from django.urls import path, include
from django.conf.urls import url
from category import views
from category.views import FolderAddView, BookmarkView, FolderEditView, FolderDelteView, TagView, TagAddView, TagEditView
app_name='category'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', BookmarkView.as_view(), name='list'),
    path('folder/edit', FolderEditView.as_view(), name='edit'),
    path('folder/add', FolderAddView.as_view(), name='add'),
    path('folder/delete', FolderDelteView.as_view(), name='delete'),
    path('tag', TagView.as_view(), name='tag'),
    path('tag/add', TagAddView.as_view(), name='tag_add'),
    path('tag/edit', TagEditView.as_view(), name='tag_edit'),
    path('tag/delete', TagView.as_view(), name='tag_delete')
]
