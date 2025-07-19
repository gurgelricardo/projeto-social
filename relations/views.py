from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Invite_Forms
from .models import Invite
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from users.forms import RegisterUser
from relations.models import Invite
from django.core.mail import send_mail
from socials.models import Post


@login_required
def create_invite(request):
    if request.method == "POST":
        invite = Invite.objects.create(sender=request.user)

        invite_url = request.build_absolute_uri(f"/invite/{invite.invite_id}/")

        messages.success(
            request,
            "Link de convite único gerado! Copie e compartilhe:",
        )
        messages.info(request, invite_url)

        return redirect("relations:create_invite")

    return render(request, "relations/create_invite.html")


def register_by_invite(request, invite_id):
    invite = get_object_or_404(Invite, invite_id=invite_id, status="PENDENTE")

    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            sender = invite.sender
            sender.relations.add(new_user)

            post_content = f"olá mundo! entrei à convite do @{sender.username}"
            Post.objects.create(author=new_user, content=post_content)

            invite.status = "ACEITO"
            invite.save()

            login(request, new_user)

            messages.success(
                request, "Cadastro concluído com sucesso! Você já está conectado(a)."
            )
            return redirect("socials:feed")

    else:
        form = RegisterUser()

    return render(request, "relations/register.html", {"form": form})
