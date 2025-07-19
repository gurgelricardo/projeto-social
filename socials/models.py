import uuid
from django.db import models
from django.conf import settings


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )

    content = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    mentions = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="mentioned_in", blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f'Post de {self.author.username} em {self.created_at.strftime("%d/%m/%Y")}'
        )
