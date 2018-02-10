"""redglasses URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from markdownx import urls as markdownx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include(markdownx)),
    path('graphql', GraphQLView.as_view(graphiql=settings.DEBUG))
]

if settings.DEBUG: # pragma: no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
