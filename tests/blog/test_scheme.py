import pytest
import graphene
from graphene.test import Client

from blog.schema import Query, TagNode, CategoryNode, PostNode
from blog.models import Tag, Category, Post
from .factory import PostFactory, CategoryFactory

schema = graphene.Schema(query=Query)

def test_tagtype():
    assert TagNode._meta.model == Tag


def test_categorytype():
    assert CategoryNode._meta.model == Category


def test_posttype():
    assert PostNode._meta.model == Post

@pytest.mark.django_db
def test_schema_post(snapshot):
    post = PostFactory.build()
    post.save()
    client = Client(schema)
    query = '''
        query {
          allPosts {
            edges {
              node {
                id
                title
                seoTitle
                slug
                locked
                live
                goLiveAt
                body
                category {
                  name
                  slug
                }
                tags {
                  edges {
                    node {
                    name
                    slug
                    }
                  }
                }
              }
            }
          }
        }
    '''
    executed = client.execute(query)
    snapshot.assert_match(executed)

@pytest.mark.django_db
def test_schema_categories(snapshot):
    cat = CategoryFactory.build()
    cat.save()
    client = Client(schema)
    query = '''
        query {
          allCategories {
            edges {
              node {
                id
                name
                slug
              }
            }
          }
        }
    '''
    executed = client.execute(query)
    snapshot.assert_match(executed)
