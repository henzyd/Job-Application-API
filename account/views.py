from django.shortcuts import render, HttpResponse


# Create your views here.

def username_or_password(request):
    return HttpResponse(request.user.username)

