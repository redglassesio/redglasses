"""Blog GraphQL scheme for blog."""
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category, Post, Tag


class TagNode(DjangoObjectType):
    """Tag Node."""
    class Meta:
        model = Tag
        filter_fields = []
        interfaces = (relay.Node, )


class CategoryNode(DjangoObjectType):
    """Category Node."""
    class Meta:
        model = Category
        filter_fields = []
        interfaces = (relay.Node, )


class PostNode(DjangoObjectType):
    """Post Node."""
    class Meta:
        model = Post
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'slug': ['exact', 'icontains'],
            'category': ['exact'],
            'category__slug': ['exact'],
            'tags': ['exact'],
            'tags__slug': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    """Blog GraphQL query."""
    all_categories = DjangoFilterConnectionField(CategoryNode)
    category = relay.Node.Field(CategoryNode)
    all_posts = DjangoFilterConnectionField(PostNode)
    post = relay.Node.Field(PostNode)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.get_live()
