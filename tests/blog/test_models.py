import pytest
from .factory import PostFactory, TagFactory, CategoryFactory


@pytest.mark.django_db
def test_post_slug():
    post = PostFactory.build()
    post.save()

    assert post.slug == 'title'


@pytest.mark.django_db
def test_tag_slug():
    tag = TagFactory.build()
    tag.save()

    assert tag.slug == 'tag-tag'


@pytest.mark.django_db
def test_category_slug():
    category = CategoryFactory.build()
    category.save()

    assert category.slug == 'category-cat'
