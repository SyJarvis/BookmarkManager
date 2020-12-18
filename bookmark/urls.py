
from django.urls import path, include
from bookmark.views import BookmarkAddView, BookmarkEditView, BookmarkDelteView, BookmarkView
app_name='bookmark'
urlpatterns = [
    path('add', BookmarkAddView.as_view(), name='add'),
    path('edit', BookmarkEditView.as_view(), name='edit'),
    path('delete', BookmarkDelteView.as_view(), name='delete'),
    path('', BookmarkView.as_view())
]
