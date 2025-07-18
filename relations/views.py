from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Invite_Forms
from .models import Invite
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from users.forms import RegisterUser
from relations.models import Invite


@login_required
def create_invite(request):
    if request.method == "POST":
        form = Invite_Forms(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data["email"]

            invite = Invite.objects.create(
                remetente=request.user, destinatario_email=recipient_email
            )

            invite_url = request.build_absolute_uri(f"/invite/{invite.id}/")

            messages.success(
                request,
                f"invite criado! Compartilhe este link: {invite_url}",
            )
            return redirect("create_invite")
    else:
        form = Invite_Forms()

    return render(request, "relations/create_invite.html", {"form": form})


def register_by_invite(request, invite_id):
    invite = get_object_or_404(Invite, id=invite_id, status="PENDENTE")

    if request.method == "POST":
        form = ReferenceError(request.POST)
        if form.is_valid():
            if form.cleaned_data["email"] != invite.destinatario_email:
                messages.error(
                    request,
                    "Erro: Você deve se cadastrar com o mesmo e-mail para o qual o invite foi enviado.",
                )
                return render(request, "usuarios/register.html", {"form": form})

            new_user = form.save()

            sender = invite.sender

            sender.conexoes.add(new_user)

            invite.status = "ACEITO"
            invite.save()

            login(request, new_user)

            messages.success(
                request, "Cadastro concluído com sucesso! Você já está conectado(a)."
            )
            return redirect("home")

    else:
        form = RegisterUser(initial={"email": invite.recipient_email})

    return render(request, "relations/register.html", {"form": form})
