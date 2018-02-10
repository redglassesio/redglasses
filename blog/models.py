"""Blog models."""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from markdownx.models import MarkdownxField

from .managers import PostManager

class AbstractTag(models.Model):
    """Abstract class for Tags and Categories."""
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=255,
        unique=True,
        editable=False,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, **kwargs): # pylint: disable=W0221
        self.slug = slugify(self.name)
        super(AbstractTag, self).save(**kwargs)

class Tag(AbstractTag):
    """Tag Model."""

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Category(AbstractTag):
    """Category Model."""

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Post(models.Model):
    """Post Model."""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='owned_pages'
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The page title as you'd like it to be seen by the public")
    )
    seo_title = models.CharField(
        verbose_name=_("page title"),
        max_length=255,
        blank=True,
        help_text=_("Optional. 'Search Engine Friendly' title.")
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        max_length=255,
        unique=True,
        editable=False,
        help_text=_("The name of the page as it will appear in URLs ")
    )
    locked = models.BooleanField(verbose_name=_('locked'), default=False)
    live = models.BooleanField(verbose_name=_('live'), default=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        null=True,
        on_delete=models.SET_NULL,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('Tag'),
        blank=True
    )
    go_live_at = models.DateTimeField(
        verbose_name=_("go live date/time"),
        blank=True,
        null=True,
        default=timezone.now
    )
    first_published_at = models.DateTimeField(
        verbose_name=_('first published at'),
        blank=True,
        null=True,
        auto_now_add=True
    )
    body = MarkdownxField()

    objects = PostManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def save(self, **kwargs): # pylint: disable=W0221
        self.slug = slugify(self.title)
        super(Post, self).save(**kwargs)
