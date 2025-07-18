from django.db import models


class Annotation(models.Model):
    note_id = models.UUIDField(
        auto_created=True,
    )
    noteContent = models.CharField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    userId = models.UUIDField
