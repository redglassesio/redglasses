"""Blog Managers."""
from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    """Post Manager."""

    def get_live(self):
        """Get only available post: lived and already went live."""
        return self.get_queryset().filter(
            live=True,
            go_live_at__lte=timezone.now()
        )
