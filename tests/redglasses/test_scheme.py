import pytest
from graphene.test import Client
from django.contrib.auth import get_user_model

from redglasses.schema import schema, UserNode
from .factory import UserFactory


def test_posttype_model():
    assert UserNode._meta.model == get_user_model()


def test_posttype_fields():
    assert list(UserNode._meta.fields.keys()) == ['username', 'first_name', 'last_name', 'id']


@pytest.mark.django_db
def test_schema_categories(snapshot):
    user = UserFactory.build()
    user.save()
    client = Client(schema)
    query = '''
    query {
      allUsers {
        edges {
          node {
            id
            username
            firstName
            lastName
          }
        }
      }
    }
    '''
    executed = client.execute(query)
    snapshot.assert_match(executed)
