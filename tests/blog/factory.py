import datetime
import factory

from django.utils.timezone import make_aware
from blog.models import Post, Tag, Category

date = make_aware(datetime.datetime(2018, 1, 5, 5, 36, 00))

class PostFactory(factory.Factory):
    class Meta:
        model = Post

    title = 'Title '
    go_live_at = date

class TagFactory(factory.Factory):
    class Meta:
        model = Tag

    name = 'Tag Tag'

class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = 'Category cat'
