from django.db import models


class User(models.Model):
    user_id = models.UUIDField(
        auto_created=True,
    )
    username = models.CharField(max_length=32, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_biography = models.TextField(blank=True, null=True, verbose_name="Biography")
    user_relations = models.ManyToManyField("self", blank=True, symmetrical=True)
