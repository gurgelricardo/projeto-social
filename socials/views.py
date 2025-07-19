from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from users.models import User
import re


@login_required
def feed(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            post = Post.objects.create(author=request.user, content=content)

            mentioned_usernames = re.findall(r"@(\w+)", content)
            for username in mentioned_usernames:
                try:
                    mentioned_user = User.objects.get(username=username)

                    post.mentions.add(mentioned_user)
                except User.DoesNotExist:
                    pass

            return redirect("socials:feed")

    posts = Post.objects.all()

    context = {"posts": posts}

    return render(request, "socials/feed.html", context)
