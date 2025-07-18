import uuid
from django.db import models
from django.conf import settings


class Invite(models.Model):
    class InviteStatus(models.TextChoices):
        CRIADO = "CRIADO", "Criado"
        PENDENTE = "PENDENTE", "Pendente"
        ACEITO = "ACEITO", "Aceito"
        EXPIRADO = "EXPIRADO", "Expirado"

    invite_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_invites"
    )
    recipient_email = models.EmailField()
    status = models.CharField(
        max_length=10, choices=InviteStatus.choices, default=InviteStatus.CRIADO
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Convite enviado de {self.sender.email} para {self.reipient_email} criado às {self.created_at}"
