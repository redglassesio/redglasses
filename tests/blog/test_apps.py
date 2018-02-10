import pytest

from blog.apps import BlogConfig

def test_apps():
    assert BlogConfig.name == "blog"