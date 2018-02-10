"""GraphQL scheme."""
from django.contrib.auth import get_user_model
from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from blog.schema import Query as PostQuery


class UserNode(DjangoObjectType):
    """
    User Node.

    limit fields for security reason
    """
    class Meta:
        model = get_user_model()
        only_fields = ('username', 'last_name', 'first_name')
        filter_fields = []
        interfaces = (relay.Node, )


class Query(PostQuery, ObjectType):
    """Public scheme."""
    all_users = DjangoFilterConnectionField(UserNode)


schema = Schema(query=Query)
