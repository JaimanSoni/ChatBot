from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Chat
from .gemini import response
# Create your views here.


def home(request):
    current_user = request.user
    chats = Chat.objects.filter(owner=request.user.id)
    if request.method == "POST":
        message = request.POST.get('message')

        ans = response(message)

        record = Chat.objects.create(
            question=message,
            answer=ans,
            owner=request.user,
        )
        record.save()
        chats = Chat.objects.filter(owner=request.user.id)

    return render(request, "files/index.html", context={'user': current_user, 'chats': chats})
