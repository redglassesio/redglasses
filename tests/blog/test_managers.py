from datetime import timedelta
import pytest
from django.utils.timezone import now
from blog.models import Post

from .factory import PostFactory


@pytest.mark.django_db
def test_get_live():

    now_date = now()
    future_date = now_date + timedelta(1)

    PostFactory.build(live=False, title="one").save()
    PostFactory.build(live=True, go_live_at=now_date, title="two").save()
    PostFactory.build(live=True, go_live_at=future_date, title="three").save()

    assert Post.objects.get_live().count() == 1


@pytest.mark.django_db
def test_get_live_not_get_future_date():

    future_date = now() + timedelta(1)

    PostFactory.build(live=True, go_live_at=future_date).save()

    assert Post.objects.get_live().count() == 0


@pytest.mark.django_db
def test_get_live_not_get_not_live():

    PostFactory.build(live=False).save()

    assert Post.objects.get_live().count() == 0
