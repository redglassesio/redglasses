"""Blog admin."""
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    """Admin Post Page."""
    list_display = ['title', 'owner', 'live', 'go_live_at', ]
    list_filter = ['live', 'go_live_at', ]
    list_select_related = ['owner', ]
    search_fields = ['title', 'body', 'seo_title']
    date_hierarchy = 'go_live_at'
    autocomplete_fields = ['tags']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin Category Page."""
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin Tag Page."""
    search_fields = ['name']
