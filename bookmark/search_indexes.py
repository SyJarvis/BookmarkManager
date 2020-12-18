# 定义索引类
from haystack import indexes
from bookmark.models import Bookmark, BookmarkForm
# 指定对于某个类的某些数据建立索引
# 索引类名格式：模型类名+Index
class BookmarkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Bookmark

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
