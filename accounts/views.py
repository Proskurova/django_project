from django.shortcuts import render


def index(request):
    return render(request, 'accounts/index.html')


def registration(request):
    return render(request, 'accounts/registration.html')