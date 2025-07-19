from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm
from django.shortcuts import get_object_or_404
from socials.models import Post
from .models import User


@login_required
def settings_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Seu perfil foi atualizado com sucesso!")
            return redirect("users:settings")
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {"form": form}
    return render(request, "users/settings.html", context)


@login_required
def profile_view(request, username):
    # Busca o usuário do perfil ou retorna um erro 404 se não existir
    profile_user = get_object_or_404(User, username=username)

    # Busca todos os posts feitos por esse usuário
    posts = Post.objects.filter(author=profile_user)

    context = {"profile_user": profile_user, "posts": posts}
    return render(request, "users/profile.html", context)
